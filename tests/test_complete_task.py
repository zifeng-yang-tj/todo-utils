"""Test for complete_task."""

import pytest

from todo_utils import TaskManager


def test_complete_task() -> None:
    """Test marking a task as completed."""
    manager = TaskManager()
    task = manager.add_task(
        title="Buy groceries",
        priority="high",
        due_date=None,
        completed=False,
    )
    completed_task = manager.complete_task(task.id)

    assert completed_task == manager.tasks[task.id]
    assert completed_task.completed


def test_complete_task_for_invalid_id() -> None:
    """Test marking a task as completed with an invalid ID."""
    manager = TaskManager()
    with pytest.raises(KeyError):
        manager.complete_task(0)