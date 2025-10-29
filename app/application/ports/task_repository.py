from __future__ import annotations
from typing import Protocol, List, Optional
from app.domain.task import Task

class TaskRepository(Protocol):
    def list(self) -> List[Task]:
        ...

    def save(self, task: Task) -> Task:
        ...

    def get(self, task_id: str) -> Optional[Task]:
        ...

    def update(self, task: Task) -> Task:
        ...

    def delete(self, task_id: str) -> None:
        ...
