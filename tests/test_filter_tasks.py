"""Test for filter_tasks."""

import pytest

from todo_utils import TaskManager


def test_filter_tasks_by_completed_status() -> None:
    """Test filtering tasks by completed status."""
    manager = TaskManager()
    manager.add_task(
        title="Buy groceries",
        priority="high",
        due_date=None,
        completed=False,
    )
    task2 = manager.add_task(
        title="Submit assignment",
        priority="medium",
        due_date=None,
        completed=True,
    )

    filtered_tasks = manager.filter_tasks(status="completed")

    assert filtered_tasks == [task2]


def test_filter_tasks_by_incomplete_status() -> None:
    """Test filtering tasks by incomplete status."""
    manager = TaskManager()
    task1 = manager.add_task(
        title="Buy groceries",
        priority="high",
        due_date=None,
        completed=False,
    )
    manager.add_task(
        title="Submit assignment",
        priority="medium",
        due_date=None,
        completed=True,
    )

    filtered_tasks = manager.filter_tasks(status="incomplete")

    assert filtered_tasks == [task1]


def test_filter_tasks_by_invalid_status() -> None:
    """Test filtering tasks with an invalid status."""
    manager = TaskManager()
    with pytest.raises(
        ValueError, match="status must be one of: completed, incomplete"
    ):
        manager.filter_tasks(status="all")


def test_filter_tasks_by_priority() -> None:
    """Test filtering tasks by priority."""
    manager = TaskManager()
    task1 = manager.add_task(
        title="Buy groceries",
        priority="high",
        due_date=None,
        completed=False,
    )
    manager.add_task(
        title="Submit assignment",
        priority="medium",
        due_date=None,
        completed=True,
    )

    filtered_tasks = manager.filter_tasks(priority="high")

    assert filtered_tasks == [task1]


def test_filter_tasks_by_invalid_priority() -> None:
    """Test filtering tasks with an invalid priority."""
    manager = TaskManager()
    with pytest.raises(
        ValueError, match="priority must be one of: low, medium, high"
    ):
        manager.filter_tasks(priority="urgent")
