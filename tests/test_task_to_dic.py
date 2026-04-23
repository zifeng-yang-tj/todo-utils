"""Test for task_to_dict."""

from datetime import date

from storage import task_to_dict
from todo_utils import Task


def test_task_to_dict() -> None:
    """Test converting a Task object to a dictionary."""
    task = Task(
        id=1,
        title="Submit assignment",
        priority="high",
        due_date=date(2024, 4, 30),
        completed=False,
    )
    result = task_to_dict(task)

    assert result == {
        "id": 1,
        "title": "Submit assignment",
        "priority": "high",
        "due_date": "2024-04-30",
        "completed": False,
    }


def test_task_to_dict_without_due_date() -> None:
    """Test converting a Task object without a due date to a dictionary."""
    task = Task(
        id=2,
        title="Buy groceries",
        priority="low",
        due_date=None,
        completed=False,
    )
    result = task_to_dict(task)

    assert result == {
        "id": 2,
        "title": "Buy groceries",
        "priority": "low",
        "due_date": None,
        "completed": False,
    }
