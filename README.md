## descriptions of its request, response and API url

# View Create Message

HTTP method: POST

Url: https://daftcodenotify.herokuapp.com/message

Authorizations: required HTTPBasic

Parameters: none

Request body schema example: application/json:

```console
{
    "content": "hello world"
}
```

Responses samples:

Status symbol: 201

Status description: successful response

Content type: application/json

Response body:

```console
{
    "msg": "You have created a message string"
}
```

Status symbol: 422

Status description: validation error

Content type: application/json

The response body for a message with character length zero:

```console
{
  "detail": [
    {
      "loc": [
        "body",
        "content"
      ],
      "msg": "ensure this value has at least 1 characters",
      "type": "value_error.any_str.min_length",
      "ctx": {
        "limit_value": 1
      }
    }
  ]
}
```

The response content for messages with a character length longer than 160:

```console
{
  "detail": [
    {
      "loc": [
        "body",
        "content"
      ],
      "msg": "ensure this value has at most 160 characters",
      "type": "value_error.any_str.max_length",
      "ctx": {
        "limit_value": 160
      }
    }
  ]
}
```


# View Show Message

HTTP method: GET

Url: https://daftcodenotify.herokuapp.com/message/{message_id}

Authorizations: not required

Path parameters: message_id, type: integer, required

Responses samples:

Status symbol: 200

Status description: successful response

Content type: application/json

Example Value:

```console
{
  "content": "hello",
  "view_counter": 1
}
```

Status symbol: 404

Status description: error: not found

Content type: application/json

```console
{
  "detail": "Message not found"
}
```

# View Update Message

HTTP method: PATCH

Url: https://daftcodenotify.herokuapp.com/message/{message_id}

Authorizations: required HTTPBasic

Path parameters: message_id, type: integer, required

Request body schema example: application/json:

```console
{
  "content": "hello again"
}
```

Responses samples:

Status symbol: 201

Status description: successful response

Content type: application/json

Example Value:

```console
{
  "content": "hello again",
  "view_counter": 0
}
```
Status symbol: 404

Status description: error: not found

Content type: application/json

```console
{
  "detail": "Message not found"
}
```

# View Delete Message

HTTP method: DELETE

Url: https://daftcodenotify.herokuapp.com/message/{message_id}

Authorizations: required HTTPBasic

Path parameters: message_id, type: integer, required

Request body schema example: application/json:

Responses samples:

Status symbol: 201

Status description: successful response

Content type: application/json

Example Value:

```console
{
  "msg": "Message id 1 has been deleted."
}
```

Status symbol: 404

Status description: error: not found

Content type: application/json

```console
{
  "detail": "Message not found"
}
```

# Check the urls in the terminal using the following commands

```console
curl --request POST -u user:access --data '{"content": "hello"}' https://daftcodenotify.herokuapp.com/message
```

```console
curl --request GET https://daftcodenotify.herokuapp.com/message/1
```

```console
curl --request PATCH -u user:access --data '{"content": "hello again"}' https://daftcodenotify.herokuapp.com/message/1
```

```console
curl --request DELETE -u user:access https://daftcodenotify.herokuapp.com/message/1
```
