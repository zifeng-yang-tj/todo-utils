"""Json storage for todo items."""

import json
from datetime import date
from pathlib import Path

from src.todo_utils import Task, TaskManager


def task_to_dict(task: Task) -> dict[str, object]:
    """Convert a Task object to a dictionary."""
    return {
        "id": task.id,
        "title": task.title,
        "priority": task.priority,
        "due_date": task.due_date.isoformat() if task.due_date else None,
        "completed": task.completed,
    }


def dict_to_task(data: dict[str, object]) -> Task:
    """Convert a dictionary to a Task object."""
    due_date = None
    if data["due_date"] is not None:
        due_date = date.fromisoformat(str(data["due_date"]))

    return Task(
        id=int(data["id"]),
        title=str(data["title"]),
        priority=str(data["priority"]),
        due_date=due_date,
        completed=bool(data["completed"]),
    )


def save_tasks(manager: TaskManager, file_path: Path) -> None:
    """Save tasks to a JSON file."""
    path = Path(file_path)
    tasks_dicts = []

    for task in manager.tasks.values():
        task_dict = task_to_dict(task)
        tasks_dicts.append(task_dict)
    with path.open("w", encoding="utf-8") as f:
        json.dump(tasks_dicts, f, indent=2)


def load_tasks(file_path: Path) -> TaskManager:
    """Load tasks from a JSON file."""
    path = Path(file_path)
    if not path.exists():
        return TaskManager()

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    tasks = {}
    for task_dict in data:
        task = dict_to_task(task_dict)
        tasks[task.id] = task
    return TaskManager(tasks=tasks)
