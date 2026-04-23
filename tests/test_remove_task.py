"""Test for remove_task."""

import pytest

from todo_utils import TaskManager


def test_remove_task() -> None:
    """Test removing a task from the manager."""
    manager = TaskManager()
    task = manager.add_task(
        title="Buy groceries",
        priority="high",
        due_date=None,
        completed=False,
    )
    removed_task = manager.remove_task(task.id)

    assert removed_task == task
    assert task.id not in manager.tasks


def test_remove_task_for_invalid_id() -> None:
    """Test removing a task with an invalid ID."""
    manager = TaskManager()
    with pytest.raises(KeyError):
        manager.remove_task(0)
