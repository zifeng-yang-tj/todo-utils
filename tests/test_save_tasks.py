"""Test for save_tasks."""

import json
from datetime import date
from pathlib import Path

from storage import save_tasks
from todo_utils import TaskManager


def test_save_tasks(tmp_path: Path) -> None:
    """Test saving tasks to a JSON file."""
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

    assert file_path.exists()


def test_save_tasks_content(tmp_path: Path) -> None:
    """Test the content of the saved JSON file."""
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

    with file_path.open(encoding="utf-8") as f:
        data = json.load(f)

    assert data == [
        {
            "id": 1,
            "title": "Submit assignment",
            "priority": "high",
            "due_date": "2024-04-30",
            "completed": False,
        },
        {
            "id": 2,
            "title": "Buy groceries",
            "priority": "low",
            "due_date": None,
            "completed": False,
        },
    ]
