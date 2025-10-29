from typing import List, Optional, Dict
from app.application.ports.task_repository import TaskRepository
from app.domain.task import Task

class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self._storage: Dict[str, Task] = {}

    def list(self) -> List[Task]:
        return list(self._storage.values())

    def save(self, task: Task) -> Task:
        self._storage[task.id] = task
        return task

    def get(self, task_id: str) -> Optional[Task]:
        return self._storage.get(task_id)

    def update(self, task: Task) -> Task:
        if task.id not in self._storage:
            raise KeyError("task not found")
        self._storage[task.id] = task
        return task

    def delete(self, task_id: str) -> None:
        if task_id in self._storage:
            del self._storage[task_id]
