import unittest

from src.modules.schedule_manager import ScheduleManager
from test.data.schedule_factory import get_schedule_with_a_single_employee #TODO: how the f* do you import this...


class TestScheduleManager(unittest.TestCase):
    def test_generate_schedule_ShouldEncodeCorrectly_whenGivenShiftObject(self):
        # Arrange
        schedule_manager = ScheduleManager()
        schedule = get_schedule_with_a_single_employee()

        # Act
        schedule_manager.generate_schedule(schedule.employees, schedule.week_start, schedule.weeks_ahead_count)

        # Assert
        #TODO: Verify that the weeks ahead of each employee has been filled 
        self.assertTrue(True)

