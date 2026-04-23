"""Command-line interface for todo utilities."""

import argparse
from collections.abc import Sequence
from datetime import date
from pathlib import Path

from storage import load_tasks, save_tasks
from todo_utils import VALID_PRIORITIES, Task


def parse_due_date(value: str) -> date:
    """Parse an ISO date from CLI input."""
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "due date must be in YYYY-MM-DD format"
        ) from exc


def format_task(task: Task) -> str:
    """Return a printable line for a task."""
    state = "done" if task.completed else "todo"
    due = task.due_date.isoformat() if task.due_date is not None else "-"
    return (
        f"{task.id:>3} | {state:<4} | {task.priority:<6} | "
        f"{due:<10} | {task.title}"
    )


def build_parser() -> argparse.ArgumentParser:
    """Build and return the CLI parser."""
    parser = argparse.ArgumentParser(
        description="Manage a to-do list from the command line."
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=Path("tasks.json"),
        help="Path to the JSON task store (default: tasks.json)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument(
        "--priority",
        choices=VALID_PRIORITIES,
        required=True,
        help="Task priority",
    )
    add_parser.add_argument(
        "--due-date",
        type=parse_due_date,
        help="Optional due date in YYYY-MM-DD format",
    )

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--status",
        choices=["completed", "incomplete"],
        help="Filter by task completion status",
    )
    list_parser.add_argument(
        "--priority",
        choices=VALID_PRIORITIES,
        help="Filter by task priority",
    )

    complete_parser = subparsers.add_parser(
        "complete", help="Mark a task as completed"
    )
    complete_parser.add_argument("task_id", type=int, help="Task id")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="Task id")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entrypoint."""
    parser = build_parser()
    args = parser.parse_args(argv)
    manager = load_tasks(args.file)

    if args.command == "add":
        task = manager.add_task(
            title=args.title,
            priority=args.priority,
            due_date=args.due_date,
        )
        save_tasks(manager, args.file)
        print(f"Added task {task.id}: {task.title}")
        return 0

    if args.command == "list":
        tasks = manager.filter_tasks(
            status=args.status,
            priority=args.priority,
        )
        if not tasks:
            print("No tasks found.")
            return 0
        print(" ID | State | Priority | Due Date   | Title")
        print("----+-------+----------+------------+----------------")
        for task in tasks:
            print(format_task(task))
        return 0

    if args.command == "complete":
        try:
            task = manager.complete_task(args.task_id)
        except KeyError:
            parser.exit(
                status=1,
                message=f"task id {args.task_id} was not found or has "
                "been removed\n",
            )
        save_tasks(manager, args.file)
        print(f"Completed task {task.id}: {task.title}")
        return 0

    if args.command == "delete":
        try:
            task = manager.remove_task(args.task_id)
        except KeyError:
            parser.exit(
                status=1,
                message=f"task id {args.task_id} was not found or has "
                "been removed\n",
            )
        save_tasks(manager, args.file)
        print(f"Deleted task {task.id}: {task.title}")
        return 0

    parser.exit(status=1, message="Unknown command\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
