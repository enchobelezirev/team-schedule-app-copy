import unittest
from mock import MagicMock
from src.models.shift import Shift
from datetime import datetime as dt
from datetime import timedelta
from parameterized import parameterized

class TestShift(unittest.TestCase):
    def test_create_shift_shouldCreateShift(self):
        # Arrange
        shift = Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9)

        # Act & Assert
        self.assertEqual(shift.start_time, dt(2022,6,10,9,30,00))
        self.assertEqual(shift.end_time, dt(2022,6,10,17,30,00))
        self.assertEqual(shift.duration, 9)

    def test_equals_shouldBeAlwaysEqual_whenStartDateAndEndDateAndDurationMatch(self):
        # Arrange
        shift1 = Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9)
        shift2 = Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9)
       
        # Act & Assert (operator)
        self.assertEqual(shift1, shift2)

        # Act & Assert (function)
        self.assertTrue(shift1.equals(shift2))

    @parameterized.expand(
        [
            ["different_start_date", Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9), Shift(dt(2022,8,10,9,30,00), dt(2022,6,10,17,30,00), 9)],
            ["different_end_date", Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9), Shift(dt(2022,6,10,9,30,00), dt(2022,9,10,17,30,00), 9)],
            ["different_duration", Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9), Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 5)],
        ]
    )
    def test_equals_shouldBeNeverEqual_whenStartDateOrEndDateOrDurationDontMatch(self, name, shift1, shift2):
        # Act & Assert (operator)
        self.assertNotEqual(shift1, shift2)

        # Act & Assert (function)
        self.assertFalse(shift1.equals(shift2))

    def test_greater_shouldBeAlwaysGreater_whenStartTimeIsGreater(self):
        # Arrange
        shift1 = Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9)
        smaller_than_shift1 = Shift(dt(2022,6,10,8,30,00), dt(2022,6,10,17,30,00), 10)

        # Act & Assert
        self.assertGreater(shift1, smaller_than_shift1)
        self.assertLess(smaller_than_shift1, shift1)

    def test_length_shouldAlwaysReturnDifferenceBetweenStartDateAndEndDate_whenStartDateIsBeforeEndDate(self):
        # Arrange
        shift = Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9)
        expected_length = timedelta(hours=8)
        
        # Act & Assert
        self.assertEqual(shift.length(), expected_length)

    def test_length_shouldAlwaysReturnZero_whenStartDateIsAfterEndDate(self):
        # Arrange
        shift = Shift(dt(2022,6,10,22,00,00), dt(2022,6,10,9,0,00), 9)
        expected_length = timedelta(hours=0)
        
        # Act & Assert
        self.assertEqual(shift.length(), expected_length)

    def test_get_matching_time_with_shift_shouldAlwaysReturnDifferece_whenTwoShiftsHaveInterectingTime(self):
        # Arrange
        shift1 = Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9)
        shift2 = Shift(dt(2022,6,10,6,30,00), dt(2022,6,10,14,30,00), 9)
        expected_matching_time = timedelta(hours=5)
        
        # Act & Assert
        self.assertEqual(shift1._Shift__get_matching_time_with_shift(shift2), expected_matching_time)

    @parameterized.expand(
        [
            ["different_years", Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9), Shift(dt(2021,6,10,9,30,00), dt(2021,6,10,17,30,00), 9)],
            ["different_months", Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9), Shift(dt(2022,7,10,9,30,00), dt(2022,7,10,17,30,00), 9)],
            ["different_days", Shift(dt(2022,6,10,9,30,00), dt(2022,6,10,17,30,00), 9), Shift(dt(2022,6,12,9,30,00), dt(2022,6,12,17,30,00), 9)],
        ]
    )
    def test_get_matching_time_with_shift_shouldAlwaysReturnTimedeltaZero_whenTwoShiftsDontHaveIntersectingTime(self, name, shift1, shift2):
        # Arrange
        expected_matching_time = timedelta(hours=0)

        # Act & Assert
        self.assertEqual(shift1._Shift__get_matching_time_with_shift(shift2), expected_matching_time)

    def test_get_matching_time_with_shifts_shouldAlwaysReturnTimedeltaDifference_whenAtLeastTwoShiftsHaveInterectingTime(self):
        # Arrange
        shift1 = Shift(dt(2022,6,11,9,00,00), dt(2022,6,11,17,00,00), 9)
        shifts = [Shift(dt(2022,6,11,6,00,00), dt(2022,6,11,14,00,00), 9) for i in range(3)] # add 3 dummy shifts
        expected_matching_time = timedelta(hours=15)
        shift1._Shift__get_matching_time_with_shift = MagicMock(return_value=timedelta(hours=5)) # for each shift use 5 as it's interection time with shift1

        # Act & Assert
        self.assertEqual(shift1.get_matching_time_with_shifts(shifts), expected_matching_time)

    def test_rest_time_shouldWork_whenFirstShiftIsBeforeSecond(self):
        # Arrange
        shift1 = Shift(dt(2022,6,11,9,00,00), dt(2022,6,11,17,00,00), 9)
        shift2 = Shift(dt(2022,6,12,9,00,00), dt(2022,6,12,17,00,00), 9)
        expected_rest_time = 16 # in hours

        # Act & Assert
        self.assertEqual(shift1.rest_time(shift2), expected_rest_time)

    def test_rest_time_shouldWork_whenFirstShiftIsAfterSecond(self):
        # Arrange
        shift1 = Shift(dt(2022,6,11,9,00,00), dt(2022,6,11,17,00,00), 9)
        shift2 = Shift(dt(2022,6,10,7,00,00), dt(2022,6,10,15,00,00), 9)
        expected_rest_time = 18 # in hours

        # Act & Assert
        self.assertEqual(shift1.rest_time(shift2), expected_rest_time)
