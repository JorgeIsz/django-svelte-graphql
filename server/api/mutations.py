from typing import Optional
import strawberry
from django.contrib.auth import authenticate

from .tokens import get_tokens
from .models import Task as TaskModel
from .types import LoginError, LoginResult, LoginSuccess, Task

def args_without_unset(args):
    return {k:v for k,v in args.items() if v is not strawberry.UNSET}

def update_task(
        self,
        id: int,
        name: Optional[str] = strawberry.UNSET,
        is_done: Optional[bool] = strawberry.UNSET,
    ) -> Task:
        task = TaskModel.objects.filter(pk=id)

        changes = args_without_unset({
            'name': name,
            'is_done': is_done,
        })

        task.update(**changes)
        return task.first()



def login(self, username: str, password: str) -> LoginResult:
    user = authenticate(username=username, password=password)

    if user is None:
        return LoginError(message="Something went wrong")

    access_token, refresh_token = get_tokens(user.pk)
    return LoginSuccess(user=user, access_token=access_token,refresh_token=refresh_token)