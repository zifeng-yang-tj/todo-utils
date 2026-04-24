# Todo Utils

Todo Utils is a lightweight Python project for managing a to-do list with:
- a reusable task management library
- a JSON persistence layer
- a command-line interface (CLI)

**Author**:
- **Zifeng Yang** (zifeng-yang-tj)
- **Ran Ji** (Ran0810)
- **Sicheng Shu** (PEARROAR)

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

## Generative AI Usage-ChatGPT

### How We Used These Tools
We used generative AI tools to support software development for this project. The tools were used for:
- help break the project into main tasks and assign tasks to members
- brainstorming project structure and feature scope
- explaining Python syntax and test design
- suggesting test cases for core functions
- helping debug import, typing, and formatting issues
- improving README and documentation wording

### What the Tools Produced
The tools produced:
- draft unit tests for storage-related functions
- explanations of existing code and test logic
- suggested Git branching and PR workflow fixes
- draft text for project documentation 

## Team Contributions

- **Zifeng Yang** implemented the core business logic, including the `Task` and `TaskManager` classes and their main methods, and set up the initial GitHub repository.
- **Ran Ji** implemented the JSON storage layer and wrote unit tests for storage and task manager functions.
- **Sicheng Shu** worked on the CLI interface, README/documentation, and contributed additional tests for CLI-related behaviors.

**Note:** In practice, to improve efficiency, team members did not strictly limit themselves to their assigned responsibilities. Some tasks were completed collaboratively, and members occasionally assisted with work outside their primary roles.