import hashlib
import secrets

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status

security = HTTPBasic()

fake_users_db = {
    'username': 'user',
    'hashed_password': 'a0561fd649cdb6baa784055f051bad796ea0afef17fca38219549deeba4e8c1a'
}


def password_hash(password: str):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def check_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(
        credentials.username, fake_users_db['username']
    )
    correct_password = secrets.compare_digest(
        password_hash(credentials.password), fake_users_db['hashed_password']
    )
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
