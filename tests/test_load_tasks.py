"""Test for load_tasks."""

from datetime import date
from pathlib import Path

from storage import load_tasks, save_tasks
from todo_utils import TaskManager


def test_load_tasks(tmp_path: Path) -> None:
    """Test loading tasks from a JSON file."""
    manager = TaskManager()
    manager.add_task(
        title="Submit assignment",
        priority="high",
        due_date=date(2024, 4, 30),
        completed=False,
    )
    manager.add_task(
        title="Buy groceries",
        priority="low",
        due_date=None,
        completed=False,
    )

    file_path = tmp_path / "tasks.json"
    save_tasks(manager, file_path)
    loaded_manager = load_tasks(file_path)

    assert loaded_manager.tasks == manager.tasks


def test_load_tasks_missing_file(tmp_path: Path) -> None:
    """Test loading tasks from a non-existent file."""
    file_path = tmp_path / "non_existent.json"
    loaded_manager = load_tasks(file_path)

    assert loaded_manager.tasks == {}
