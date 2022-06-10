import math
from datetime import datetime, timedelta
from typing import List
from src.modules.restriction_manager.restriction_manager import ShiftRestrictionManager

from src.models.employee import Employee
from src.models.shift import Shift
from src.modules.schedule_generator.shift_frequency_generator.models.week_shift import WeekShift


class ShiftFrequencyGenerator:
    def __init__(self):
        self.shift_restriction_manager = ShiftRestrictionManager()

    def generate_schedule(
        self, employees: List[Employee], week_start: datetime, weeks_ahead_count: int, availableSlots=None
    ):
        """
        Generate the shifts for N weeks ahead.
        """
        for i in range(weeks_ahead_count):
            self.create_weekly_schedule(employees, week_start)
            week_start += timedelta(days=7)

    def create_weekly_schedule(self, employees: List[Employee], week_start: datetime, available_slots=None):
        """
        Create schedule for given week

        Parameters:
        ----------
        employees: list of employees to be scheduled, each containing working hours and shifts in the past 6 months
        week_start: week start date
        available_slots: for this case, all slots are available. in the future we can implement functions for predefined slots
        """
        for employee in employees:
            self._assign_shifts_given_employee(employee, week_start)

    def _assign_shifts_given_employee(self, employee: Employee, week_start: datetime):
        """
        Implementation of the simples case of assigning a single employee.
        """
        # Here we can add any other of the ideas we discussed
        return self._infinite_potential_idea(employee, week_start)

    def _infinite_potential_idea(self, employee: Employee, week_start: datetime) -> List[Shift]:
        # shiftCandidates = Take all employee possible shifts
        week_shift_weights = self._get_weighted_week_shift_counts(employee, week_start)
        weekshifts = list(week_shift_weights.keys())
        current_hours = 0

        # while current_hours < weekly_hours
        while current_hours < employee.weekly_hours and len(week_shift_weights) > 0:
            # pick the top slot
            topWeeklyShift = next(iter(week_shift_weights))
            topShift = Shift.from_weekshift(topWeeklyShift, week_start)

            current_hours += topShift.duration / 60
            employee.next_week_shifts.append(topShift)
            # remove illegal shifts according to filled ones
            weekshifts = set(self._remove_illegal_shifts(employee, weekshifts, week_start))
            # reorder the shift's preference_score (if taking times taken, it's not needed) - evalute_shift_preference()
            week_shift_weights = {weekshift: week_shift_weight for weekshift, week_shift_weight in week_shift_weights.items() if weekshift in weekshifts}


    def _remove_illegal_shifts(self, employee: Employee, week_shift_andidates: List[Shift], week_start: datetime) -> List[Shift]:
        filtered_shifts = week_shift_andidates.copy()

        for week_shift_candidate in week_shift_andidates:
            shift_candidate = Shift.from_weekshift(week_shift_candidate, week_start)
            if not self.shift_restriction_manager.is_shift_allowed(employee, shift_candidate):
                filtered_shifts.remove(week_shift_candidate)

        return filtered_shifts

    def _get_weighted_week_shift_counts(self, employee: Employee, week_start: datetime):
        shifts = employee.past_shifts + employee.next_week_shifts
        weighted_week_shifts = {}
        for shift in shifts:
            weekshift = WeekShift(
                shift.start_time.weekday(),
                shift.start_time.hour,
                shift.duration,
                (shift.end_time - shift.start_time).seconds / 60,
            )
            if weekshift not in weighted_week_shifts.keys():
                weighted_week_shifts[weekshift] = self._get_weighed_shift(weekshift, shifts, week_start)
        return dict(sorted(weighted_week_shifts.items(), key=lambda item: item[1], reverse=True))

    def _get_weighed_shift(self, week_shift: WeekShift, shifts: List[Shift], week_start: datetime) -> float:
        # TODO implement "shift_frequency" function here
        return sum(
            [self._timespan_weight(week_start - shift.start_time) for shift in shifts if week_shift.matches_shift(shift)]
        )

    def _timespan_weight(self, timediff):
        w = float(abs(timediff.days)) / 7.0
        return math.exp(-w)
