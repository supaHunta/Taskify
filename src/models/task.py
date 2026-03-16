from pydantic import BaseModel
from datetime import datetime
from typing import List
from src.models.checklist import ChecklistItem

class Task(BaseModel):
    title: str
    description: str
    id: str
    status: str = "pending"
    priority: str = "medium"
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    checklist: List[ChecklistItem] | None = None
