"""Test for dict_to_task."""

from datetime import date

from storage import dict_to_task
from todo_utils import Task


def test_dict_to_task() -> None:
    """Test converting a dictionary to a Task object."""
    data = {
        "id": 1,
        "title": "Submit assignment",
        "priority": "high",
        "due_date": "2024-04-30",
        "completed": False,
    }
    result = dict_to_task(data)

    assert result == Task(
        id=1,
        title="Submit assignment",
        priority="high",
        due_date=date(2024, 4, 30),
        completed=False,
    )


def test_dict_to_task_without_due_date() -> None:
    """Test converting a dictionary to a Task object without a due date."""
    data = {
        "id": 2,
        "title": "Buy groceries",
        "priority": "low",
        "due_date": None,
        "completed": False,
    }
    result = dict_to_task(data)

    assert result == Task(
        id=2,
        title="Buy groceries",
        priority="low",
        due_date=None,
        completed=False,
    )
