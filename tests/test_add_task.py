"""Test function add_task."""

import pytest

from todo_utils import TaskManager


def test_add_task() -> None:
    """Test adding a task to the manager."""
    manager = TaskManager()
    task = manager.add_task(
        title="Buy groceries",
        priority="high",
        due_date=None,
        completed=False,
    )
    assert task.id == 1
    assert task.title == "Buy groceries"
    assert task.priority == "high"
    assert task.due_date is None
    assert not task.completed


def test_add_task_for_invalid_priority() -> None:
    """Test adding a task with an invalid priority."""
    manager = TaskManager()
    with pytest.raises(
        ValueError, match="priority must be one of: low, medium, high"
    ):
        manager.add_task(
            title="Buy groceries",
            priority="urgent",
            due_date=None,
            completed=False,
        )


def test_add_task_for_empty_title() -> None:
    """Test adding a task with an empty title."""
    manager = TaskManager()
    with pytest.raises(ValueError, match="title must not be empty"):
        manager.add_task(
            title="   ",
            priority="low",
            due_date=None,
            completed=False,
        )
