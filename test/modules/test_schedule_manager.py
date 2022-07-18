import unittest
from src.modules.schedule_manager import ScheduleManager
from test.data.schedule_factory import get_schedule_with_a_single_employee
from datetime import timedelta



class TestScheduleManager(unittest.TestCase):
    def test_generate_schedule_ShouldGenerateScheduleForGivenWeaksCount_whenCalledWithCorrectData(self):
        # Arrange
        schedule_manager = ScheduleManager()
        schedule = get_schedule_with_a_single_employee()

        # Act
        schedule_manager.generate_schedule(schedule.employees, schedule.week_start, schedule.weeks_ahead_count)

        # Assert
        for shift in schedule.employees[0].next_week_shifts:
            self.assertTrue(shift.start_time >= schedule.week_start)
            self.assertTrue(shift.start_time <= schedule.week_start + timedelta(days=28))

