import unittest
import json
from src.models.schedule import Schedule
from src.modules.api_mapper.api_mapper import map_request_to_classes
from datetime import datetime, timedelta

ONE_EMPLOYEE_SCHEDULE_PATH = "test/data/sample_files/manager_single_employee.json"

class TestApiMapper(unittest.TestCase):
    def test_map_request_to_classes_Should_create_correct_schedule_object(self):
        # Arrange
        with open(ONE_EMPLOYEE_SCHEDULE_PATH, "r", encoding="utf-8") as file:
            sample_json = json.load(file)

        # Act
        schedule = map_request_to_classes(sample_json)

        # Assert
        self.assertEqual(type(schedule), Schedule)
        self.assertEqual(schedule.manager_id, "0")
        self.assertEqual(len(schedule.employees), 1)
        self.assertEqual(len(schedule.employees[0].past_shifts), 2)
        self.assertEqual(len(schedule.employees[0].next_week_shifts), 0)
        self.assertEqual(schedule.employees[0].uid, "U001072")
        self.assertEqual(schedule.employees[0].past_shifts[0].end_time, datetime(2021, 5, 24, 18, 0))
        self.assertEqual(schedule.employees[0].past_shifts[0].start_time, datetime(2021, 5, 24, 9, 0))
        self.assertEqual(schedule.employees[0].past_shifts[0].duration, 480)
