from typing import List

from .types import Task
from .models import Task as TaskModel
from .decorators import auth_required

@auth_required
def get_tasks(self, info) -> List[Task]:
    user = info.context.request.user
    return TaskModel.objects.filter(user=user)
