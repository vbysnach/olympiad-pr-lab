from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.statistics import median_minutes


class EvenMedianTests(unittest.TestCase):
    def test_even_sized_median_is_average_of_middle_values(self) -> None:
        first = StudyTask("A-1", "First", 30, "high", date(2026, 9, 20))
        second = StudyTask("A-2", "Second", 60, "medium", date(2026, 9, 21))

        self.assertEqual(45.0, median_minutes([first, second]))
