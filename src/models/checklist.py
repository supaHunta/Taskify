from pydantic import BaseModel

class ChecklistItem(BaseModel):
    emoji: str = None
    title: str
    isDone: bool = False