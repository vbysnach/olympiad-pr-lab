from datetime import date
import unittest

from study_planner.records import task_from_record


class OptionalRecordCompletionTests(unittest.TestCase):
    def test_missing_record_completion_defaults_to_false(self) -> None:
        task = task_from_record(
            {
                "task_id": "A-1",
                "title": "Minimal",
                "minutes": 30,
                "priority": "high",
                "due_date": date(2026, 9, 20).isoformat(),
            }
        )

        self.assertFalse(task.completed)
