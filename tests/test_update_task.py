"""Test for update_task."""

import pytest

from todo_utils import TaskManager


def test_update_task() -> None:
    """Test updating a task in the manager."""
    manager = TaskManager()
    task = manager.add_task(
        title="Buy groceries",
        priority="low",
        due_date=None,
        completed=False,
    )
    updated_task = manager.update_task(
        task_id=task.id,
        title="Buy groceries and submit assignment",
        priority="high",
        due_date=None,
        completed=True,
    )

    assert updated_task.title == "Buy groceries and submit assignment"
    assert updated_task.priority == "high"
    assert updated_task.due_date is None
    assert updated_task.completed is True


def test_update_task_for_invalid_id() -> None:
    """Test updating a task with an invalid ID."""
    manager = TaskManager()
    with pytest.raises(KeyError):
        manager.update_task(
            task_id=0,
            title="Buy groceries and submit assignment",
            priority="high",
            due_date=None,
            completed=True,
        )


def test_update_task_for_invalid_priority() -> None:
    """Test updating a task with an invalid priority."""
    manager = TaskManager()
    task = manager.add_task(
        title="Buy groceries",
        priority="low",
        due_date=None,
        completed=False,
    )
    with pytest.raises(
        ValueError, match="priority must be one of: low, medium, high"
    ):
        manager.update_task(
            task_id=task.id,
            title="Buy groceries and submit assignment",
            priority="urgent",
            due_date=None,
            completed=True,
        )


def test_update_task_for_empty_title() -> None:
    """Test updating a task with an empty title."""
    manager = TaskManager()
    task = manager.add_task(
        title="Buy groceries",
        priority="low",
        due_date=None,
        completed=False,
    )
    with pytest.raises(ValueError, match="title must not be empty"):
        manager.update_task(
            task_id=task.id,
            title="   ",
            priority="high",
            due_date=None,
            completed=True,
        )
