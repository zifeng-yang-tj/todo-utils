"""Test for clear_completed_tasks."""

from todo_utils import TaskManager


def test_clear_completed_tasks() -> None:
    """Test clearing completed tasks from the manager."""
    manager = TaskManager()
    task1 = manager.add_task(
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

    removed_tasks = manager.clear_completed_tasks()

    assert removed_tasks == [task2]
    assert task1.id in manager.tasks
    assert task2.id not in manager.tasks


def test_clear_completed_tasks_with_no_completed_tasks() -> None:
    """Test clearing completed tasks when there are no completed tasks."""
    manager = TaskManager()
    task1 = manager.add_task(
        title="Buy groceries",
        priority="high",
        due_date=None,
        completed=False,
    )
    task2 = manager.add_task(
        title="Submit assignment",
        priority="medium",
        due_date=None,
        completed=False,
    )

    removed_tasks = manager.clear_completed_tasks()

    assert removed_tasks == []
    assert task1.id in manager.tasks
    assert task2.id in manager.tasks
