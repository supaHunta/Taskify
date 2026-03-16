from src.models.task import Task
from typing import List

class TaskActions:
    def create_task(self, title: str, description: str) -> Task:
        return Task(title=title, description=description)
    
    def update_task(self, task: Task) -> bool:
        return True
    
    def delete_task(self, task: Task) -> bool:
        return True
    
    def get_task(self, task: Task) -> Task:
        pass
    
    def get_all_tasks(self) -> List[Task]:
        pass