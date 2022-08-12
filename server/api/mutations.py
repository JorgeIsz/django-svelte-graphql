from typing import Optional
import strawberry

from .models import Task as TaskModel
from .types import Task

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

