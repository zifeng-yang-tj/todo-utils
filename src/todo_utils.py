"""To-do list management utilities."""

from datetime import date

VALID_PRIORITIES: tuple[str, ...] = ("low", "medium", "high")
PRIORITY_ORDER: dict[str, int] = {
    "high": 0,
    "medium": 1,
    "low": 2,
}


class Task:
    """Represents a single to-do item."""

    def __init__(
        self,
        id: int,
        title: str,
        priority: str,
        due_date: date | None = None,
        completed: bool = False,
    ) -> None:
        """Initialize a single to-do item."""
        self.id = id
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __repr__(self) -> str:
        """Return a string representation of the task."""
        return (
            f"Task(id={self.id}, title={self.title!r}, "
            f"priority={self.priority!r}, due_date={self.due_date}, "
            f"completed={self.completed})"
        )

    def __eq__(self, other: object) -> bool:
        """Compare two tasks for equality."""
        if not isinstance(other, Task):
            return NotImplemented
        return (
            self.id == other.id
            and self.title == other.title
            and self.priority == other.priority
            and self.due_date == other.due_date
            and self.completed == other.completed
        )


class TaskManager:
    """Manages a list of to-do items."""

    def __init__(self, tasks: dict[int, Task] | None = None) -> None:
        """Initialize the manager with optional existing tasks."""
        initial_tasks = {} if tasks is None else tasks
        self.tasks: dict[int, Task] = initial_tasks
        self.occupied_ids: set[int] = {id for id in initial_tasks}
        self.next_id: int = self._compute_next_id()

    def _compute_next_id(self) -> int:
        """Return the next available task id."""
        if not self.occupied_ids:
            return 1
        return max(self.occupied_ids) + 1

    def add_task(
        self,
        title: str,
        priority: str,
        due_date: date | None = None,
        completed: bool = False,
    ) -> Task:
        """Create and store a new task."""
        if priority not in VALID_PRIORITIES:
            raise ValueError("priority must be one of: low, medium, high")

        normalized_title = title.strip()
        if not normalized_title:
            raise ValueError("title must not be empty")

        task = Task(
            id=self.next_id,
            title=normalized_title,
            priority=priority,
            due_date=due_date,
            completed=completed,
        )
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def _get_task_by_id(self, task_id: int) -> Task:
        """Return a task by id or raise a clear error."""
        if task_id not in self.tasks:
            raise KeyError(
                f"task id {task_id} was not found or has been removed"
            )
        return self.tasks[task_id]

    def remove_task(self, task_id: int) -> Task:
        """Remove a task by id and return it."""
        task = self._get_task_by_id(task_id)
        del self.tasks[task_id]
        return task

    def complete_task(self, task_id: int) -> Task:
        """Mark a task as completed and return it."""
        task = self._get_task_by_id(task_id)
        task.completed = True
        return task

    def clear_completed_tasks(self) -> list[Task]:
        """Remove all completed tasks and return them."""
        completed_tasks = [
            task for task in self.tasks.values() if task.completed
        ]
        for task in completed_tasks:
            del self.tasks[task.id]
        return completed_tasks

    def update_task(
        self,
        task_id: int,
        title: str | None = None,
        priority: str | None = None,
        due_date: date | None = None,
        completed: bool | None = None,
    ) -> Task:
        """Update fields of a task and return it."""
        task = self._get_task_by_id(task_id)

        if title is not None:
            normalized_title = title.strip()
            if not normalized_title:
                raise ValueError("title must not be empty")
            task.title = normalized_title

        if priority is not None:
            if priority not in VALID_PRIORITIES:
                raise ValueError("priority must be one of: low, medium, high")
            task.priority = priority

        if due_date is not None:
            task.due_date = due_date

        if completed is not None:
            task.completed = completed

        return task

    @staticmethod
    def _sort_key(task: Task) -> tuple[bool, bool, date, int, int]:
        """Build the ordering key for task listings.

        Tasks are ordered by:
        1. Incomplete before completed
        2. Tasks with due dates before those without
        3. Earlier due dates before later ones
        4. Higher priority before lower
        5. Lower id before higher
        """
        due_date = task.due_date if task.due_date is not None else date.max
        return (
            task.completed,
            task.due_date is None,
            due_date,
            PRIORITY_ORDER[task.priority],
            task.id,
        )

    def list_tasks(self) -> list[Task]:
        """Return all tasks in display order."""
        return sorted(self.tasks.values(), key=self._sort_key)

    def filter_tasks(
        self,
        status: str | None = None,
        priority: str | None = None,
    ) -> list[Task]:
        """Return tasks that match the provided filters."""
        if status not in (None, "completed", "incomplete"):
            raise ValueError("status must be one of: completed, incomplete")

        if priority is not None and priority not in VALID_PRIORITIES:
            raise ValueError("priority must be one of: low, medium, high")

        filtered_tasks = list(self.tasks.values())
        if status == "completed":
            filtered_tasks = [
                task for task in filtered_tasks if task.completed
            ]
        elif status == "incomplete":
            filtered_tasks = [
                task for task in filtered_tasks if not task.completed
            ]

        if priority is not None:
            filtered_tasks = [
                task for task in filtered_tasks if task.priority == priority
            ]

        return sorted(filtered_tasks, key=self._sort_key)
