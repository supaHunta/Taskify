from pydantic import BaseModel
from datetime import datetime
from typing import List
from src.models.checklist import ChecklistItem
from uuid import uuid4

class Task(BaseModel):
    title: str
    description: str
    id: str = str(uuid4())#ToDo: Add a better id generator
    status: str = "pending"#ToDo: Add a better status generator
    priority: str = "medium"#ToDo: Add a better priority generator
    created_at: datetime = datetime.now()#ToDo: Add a better created_at generator
    updated_at: datetime = datetime.now()#ToDo: Add a better updated_at generator
    checklist: List[ChecklistItem] | None = None#ToDo: Add a better checklist generator
