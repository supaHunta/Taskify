import pytest

from src.business_logic.task_manager import TaskActions

class TestTaskActions:
    def test_create_task(self):
        task_actions = TaskActions()
        task = task_actions.create_task("Test Task", "This is a test task")
        assert task.title == "Test Task"
        assert task.description == "This is a test task"
        assert task.status == "pending"
        assert task.priority == "medium"
        assert task.created_at is not None
        assert task.updated_at is not None
        assert task.checklist is None

    def test_update_task(self):
        task_actions = TaskActions()
        task = task_actions.create_task("Test Task", "This is a test task")
        task_actions.update_task(task, title="Updated Task", description="This is an updated task")
        assert task.title == "Updated Task"
        assert task.description == "This is an updated task"
        assert task.status == "pending"
        assert task.priority == "medium"
        assert task.created_at is not None
        assert task.updated_at is not None
        assert task.checklist is None