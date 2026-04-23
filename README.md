# Todo Utils

Todo Utils is a lightweight Python project for managing a to-do list with:
- a reusable task management library
- a JSON persistence layer
- a command-line interface (CLI)

## Installation

1. Clone the repository.

```bash
git clone https://github.com/zifeng-yang-tj/todo-utils.git
cd todo-utils
```

2. Install dependencies.

```bash
pip install -r requirements-test.txt
```

## Usage

Run commands from the repository root:

```bash
python src/todo_cli.py --help
```

By default, tasks are stored in `tasks.json` in the current directory.
You can override it with `--file`.

### Add a task

```bash
python src/todo_cli.py add "Buy groceries" --priority high
python src/todo_cli.py add "Pay rent" --priority medium --due-date 2026-05-01
```

### List tasks

```bash
python src/todo_cli.py list
```

### Complete a task

```bash
python src/todo_cli.py complete 1
```

### Delete a task

```bash
python src/todo_cli.py delete 2
```

### Filter options

Filter while listing:

```bash
python src/todo_cli.py list --status completed
python src/todo_cli.py list --status incomplete
python src/todo_cli.py list --priority high
python src/todo_cli.py list --status incomplete --priority medium
```

## Run Tests

Run all tests:

```bash
pytest
```

Run with coverage:

```bash
coverage run --source=src -m pytest
coverage report -m
```

## Project Architecture

- `src/todo_utils.py`: domain layer
  - `Task`: task entity
  - `TaskManager`: core business logic (add/update/delete/complete/list/filter)
- `src/storage.py`: persistence layer
  - serialization and deserialization between `Task` and JSON
  - read/write task data from disk
- `src/todo_cli.py`: interface layer
  - parses CLI commands and options
  - invokes `TaskManager` operations
  - saves updated state to JSON
- `tests/`: automated tests for manager logic and CLI behavior
- `.github/workflows/`: CI for lint/type checks, tests, and coverage reporting
