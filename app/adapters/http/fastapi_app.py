from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator
from typing import List
from app.adapters.persistence.memory_task_repository import InMemoryTaskRepository
from app.application.services.task_service import TaskService
from app.domain.task import Status, Task as DomainTask

app = FastAPI(title="Tasks API - Exam")

# Pydantic schemas
class TaskIn(BaseModel):
    title: str = Field(..., min_length=1)
    status: str = Field(default=Status.pending.value)

    @field_validator("status")
    def check_status(cls, v):
        if v not in (Status.pending.value, Status.done.value):
            raise ValueError("status must be 'pending' or 'done'")
        return v

class TaskOut(BaseModel):
    id: str
    title: str
    status: str

# Wiring (simple)
repo = InMemoryTaskRepository()
service = TaskService(repo)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks", response_model=List[TaskOut])
def list_tasks():
    tasks = service.list_tasks()
    return [TaskOut(id=t.id, title=t.title, status=t.status.value) for t in tasks]

@app.post("/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(body: TaskIn):
    try:
        task = service.create_task(title=body.title, status=body.status)
        return TaskOut(id=task.id, title=task.title, status=task.status.value)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: str):
    t = service.get_task(task_id)
    if not t:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskOut(id=t.id, title=t.title, status=t.status.value)

@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: str, body: TaskIn):
    try:
        updated = service.update_task(task_id, title=body.title, status=body.status)
        if not updated:
            raise HTTPException(status_code=404, detail="Task not found")
        return TaskOut(id=updated.id, title=updated.title, status=updated.status.value)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: str):
    ok = service.delete_task(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return
