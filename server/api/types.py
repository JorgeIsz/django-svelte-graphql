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
