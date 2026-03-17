from src.models.task import Task
from typing import List
from src.models.checklist import ChecklistItem

class TaskActions:
    def create_task(self, title: str, description: str) -> Task:
        return Task(title=title, description=description)
    
    def update_task(self, task: Task, title: str = None, description: str = None, status: str = None, priority: str = None, checklist: List[ChecklistItem] = None) -> bool:
        if title:
            task.title = title
        if description:
            task.description = description
        if status:
            task.status = status
        if priority:
            task.priority = priority
        if checklist:
            task.checklist = checklist
    
    def delete_task(self, task: Task) -> bool:
        return True
    
    def get_task(self, task: Task) -> Task:
        pass
    
    def get_all_tasks(self) -> List[Task]:
        pass