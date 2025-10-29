from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
import uuid

class Status(str, Enum):
    pending = "pending"
    done = "done"

@dataclass
class Task:
    id: str
    title: str
    status: Status = Status.pending

    @staticmethod
    def create(title: str, status: str | Status = Status.pending) -> "Task":
        if not title or not title.strip():
            raise ValueError("title is required and must not be empty")
        try:
            st = Status(status) if not isinstance(status, Status) else status
        except Exception:
            raise ValueError("status must be 'pending' or 'done'")
        return Task(id=str(uuid.uuid4()), title=title.strip(), status=st)
