from typing import List
import strawberry

from .types import User, Task, LoginResult
from .queries import get_tasks
from .mutations import update_task, login

@strawberry.type
class Query:
    user: User = strawberry.django.field()
    tasks: List[Task] = strawberry.django.field(resolver=get_tasks)


@strawberry.type
class Mutation:
    update_task: Task = strawberry.django.field(resolver=update_task)
    login: LoginResult = strawberry.django.field(resolver=login)
    
schema = strawberry.Schema(query=Query, mutation=Mutation)
