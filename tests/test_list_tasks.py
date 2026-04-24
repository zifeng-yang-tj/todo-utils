"""Test for list_tasks."""

from datetime import date

from todo_utils import TaskManager


def test_list_tasks() -> None:
    """Test list_tasks in the correct way."""
    manager = TaskManager()
    task1 = manager.add_task(
        title="Buy groceries",
        priority="low",
        due_date=None,
        completed=False,
    )
    task2 = manager.add_task(
        title="Submit assignment",
        priority="high",
        due_date=date(2024, 4, 30),
        completed=False,
    )

    tasks = manager.list_tasks()

    assert tasks == [task2, task1]


def test_list_tasks_with_no_tasks() -> None:
    """Test list_tasks when there are no tasks."""
    manager = TaskManager()

    tasks = manager.list_tasks()

    assert tasks == []
