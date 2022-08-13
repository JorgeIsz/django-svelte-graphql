import strawberry
from strawberry import auto

from . import models

@strawberry.django.type(models.User)
class User:
    id: auto
    name: auto
    username: auto

@strawberry.django.type(models.Task)
class Task:
    id: auto
    name: auto
    is_done: auto

@strawberry.type
class LoginSuccess:
    user: User
    access_token: str
    refresh_token: str

@strawberry.type
class LoginError:
    message: str


LoginResult = strawberry.union("LoginResult", (LoginSuccess, LoginError))

