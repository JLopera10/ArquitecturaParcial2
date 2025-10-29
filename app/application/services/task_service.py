from typing import List, Optional
from app.domain.task import Task
from app.application.ports.task_repository import TaskRepository

class TaskService:
    def __init__(self, repo: TaskRepository):
        self._repo = repo

    def list_tasks(self) -> List[Task]:
        return self._repo.list()

    def create_task(self, title: str, status: str | None = None) -> Task:
        task = Task.create(title=title, status=status or Task().status if False else (status or "pending"))
        # The creation validated inputs
        return self._repo.save(task)

    def get_task(self, task_id: str) -> Optional[Task]:
        return self._repo.get(task_id)

    def update_task(self, task_id: str, title: str | None = None, status: str | None = None) -> Optional[Task]:
        task = self._repo.get(task_id)
        if not task:
            return None
        new_title = title if title is not None else task.title
        new_status = status if status is not None else task.status.value
        updated = Task(id=task.id, title=new_title, status=Task.create(new_title, new_status).status)
        return self._repo.update(updated)

    def delete_task(self, task_id: str) -> bool:
        existing = self._repo.get(task_id)
        if not existing:
            return False
        self._repo.delete(task_id)
        return True
