from typing import List,Optional
import strawberry

from .types import User, Task
from .models import Task as TaskModel
from .queries import get_tasks
from .mutations import update_task

@strawberry.type
class Query:
    user: User = strawberry.django.field()
    tasks: List[Task] = strawberry.django.field(resolver=get_tasks)


@strawberry.type
class Mutation:
    update_task: Task = strawberry.django.field(resolver=update_task)
    
schema = strawberry.Schema(query=Query, mutation=Mutation)
