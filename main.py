from typing import ClassVar, Dict, Optional

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field, PrivateAttr

from security import check_credentials


class Message(BaseModel):
    _id: Optional[int] = PrivateAttr()
    counter: ClassVar[int] = 1
    content: str = Field(min_length=1, max_length=160)
    _view_counter: Optional[int] = PrivateAttr(0)

    def add_view(self):
        self._view_counter += 1

    def show_view_counter(self):
        return self._view_counter


class HelloResp(BaseModel):
    msg: str


app = FastAPI()
app.storage: Dict[int, Message] = {}


@app.post('/message', status_code=201, response_model=HelloResp)
async def create_message(message: Message,
                         dependencies=Depends(check_credentials)):
    message._id = Message.counter
    app.storage[Message.counter] = message
    Message.counter += 1
    return HelloResp(msg=f'You have created a message {message.content}')


@app.get('/message/{message_id}')
async def show_message(message_id: int):
    if message_id not in app.storage:
        raise HTTPException(status_code=404, detail='Message not found')
    message = app.storage.get(message_id)
    message.add_view()
    return {
        'content': message.content,
        'view_counter': message.show_view_counter()
    }


@app.patch('/message/{message_id}')
async def update_message(message_id: int, message: Message,
                         dependencies=Depends(check_credentials)):
    if message_id not in app.storage:
        raise HTTPException(status_code=404, detail='Message not found')
    app.storage[message_id] = message
    message._view_counter = 0
    return {
        'content': message.content,
        'view_counter': message.show_view_counter()
    }


@app.delete('/message/{message_id}', status_code=201, response_model=HelloResp)
async def delete_message(message_id: int,
                         dependencies=Depends(check_credentials)):
    if message_id not in app.storage:
        raise HTTPException(status_code=404, detail='Message not found')
    del app.storage[message_id]
    return HelloResp(msg=f'Message id {message_id} has been deleted.')
