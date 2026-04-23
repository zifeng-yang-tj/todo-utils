"""Tests for the command-line interface."""

from pathlib import Path

import pytest

from todo_cli import main


def run_cli(args: list[str], store_path: Path) -> int:
    """Run CLI command with a dedicated store path."""
    return main(["--file", str(store_path), *args])


def test_add_and_list_tasks(capsys: pytest.CaptureFixture[str]) -> None:
    """Add tasks and verify list output."""
    store_path = Path("tasks_test_add_list.json")
    try:
        result = run_cli(
            ["add", "Buy milk", "--priority", "high"],
            store_path=store_path,
        )
        assert result == 0

        result = run_cli(
            [
                "add",
                "Read book",
                "--priority",
                "low",
                "--due-date",
                "2026-05-01",
            ],
            store_path=store_path,
        )
        assert result == 0

        result = run_cli(["list"], store_path=store_path)
        assert result == 0
        output = capsys.readouterr().out
        assert "Buy milk" in output
        assert "Read book" in output
    finally:
        if store_path.exists():
            store_path.unlink()


def test_complete_and_filter(capsys: pytest.CaptureFixture[str]) -> None:
    """Mark task complete and filter by status."""
    store_path = Path("tasks_test_complete.json")
    try:
        run_cli(["add", "Task A", "--priority", "medium"], store_path)
        run_cli(["add", "Task B", "--priority", "low"], store_path)

        result = run_cli(["complete", "1"], store_path)
        assert result == 0

        result = run_cli(
            ["list", "--status", "completed"],
            store_path=store_path,
        )
        assert result == 0
        output = capsys.readouterr().out
        assert "Task A" in output
        assert "Task B" not in output
    finally:
        if store_path.exists():
            store_path.unlink()


def test_delete_task(capsys: pytest.CaptureFixture[str]) -> None:
    """Delete a task by id."""
    store_path = Path("tasks_test_delete.json")
    try:
        run_cli(["add", "Task C", "--priority", "medium"], store_path)

        result = run_cli(["delete", "1"], store_path)
        assert result == 0

        result = run_cli(["list"], store_path)
        assert result == 0
        output = capsys.readouterr().out
        assert "No tasks found." in output
    finally:
        if store_path.exists():
            store_path.unlink()
