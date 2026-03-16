from pydantic import BaseModel

class ChecklistItem(BaseModel):
    title: str
    isDone: bool = False