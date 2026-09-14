"""In-memory record conversion helpers for study tasks."""

from datetime import date
from typing import Dict, Mapping, Union

from .planner import StudyTask


RecordValue = Union[str, int, bool]


def task_to_record(task: StudyTask) -> Dict[str, RecordValue]:
    """Convert a task to a simple record with a boolean completion field."""
    return {
        "task_id": task.task_id,
        "title": task.title,
        "minutes": task.minutes,
        "priority": task.priority,
        "due_date": task.due_date.isoformat(),
        "completed": task.completed,
    }


def task_from_record(record: Mapping[str, RecordValue]) -> StudyTask:
    """Build a task from a record; missing ``completed`` means ``False``."""
    return StudyTask(
        task_id=str(record["task_id"]),
        title=str(record["title"]),
        minutes=int(record["minutes"]),
        priority=str(record["priority"]),
        due_date=date.fromisoformat(str(record["due_date"])),
        completed=bool(record.get("completed", False)),
    )
