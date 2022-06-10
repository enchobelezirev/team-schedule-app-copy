import math
from datetime import datetime, timedelta
from typing import List

from src.models.employee import Employee
from src.models.shift import Shift
from src.modules.schedule_generator.shift_frequency_generator.models.week_shift import WeekShift


class ShiftFrequencyGenerator:
    def __init__(self):
        pass

    def generate_schedule(self, employees: List[Employee], week_start: datetime, weeks_ahead_count: int, available_slots=None):
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
        # shift_candidates = Take all employee possible shifts
        employee_shifts = employee.past_shifts + employee.next_week_shifts
        week_shift_weights = self._get_weighted_week_shift_counts(employee_shifts, week_start)
        week_shifts = set([week_shift for week_shift, week_shift_weight in week_shift_weights.items()])
        current_hours = 0
        chosen_shifts = []

        # while current_hours < weekly_hours
        while current_hours < employee.weekly_hours and len(week_shift_weights) > 0:
            # pick the top slot
            top_weekly_shift = next(iter(week_shift_weights))
            top_shift = Shift(
                week_start + timedelta(days=top_weekly_shift.weekday, hours=top_weekly_shift.start_time),
                week_start + timedelta(days=top_weekly_shift.weekday, hours=top_weekly_shift.start_time + top_weekly_shift.fullDuration / 60),
                top_weekly_shift.duration,
            )
            current_hours += top_shift.duration / 60
            chosen_shifts.append(top_shift)
            # remove illegal shifts according to filled ones
            week_shifts = set(self._remove_illegal_shifts(chosen_shifts, week_shifts, week_start))
            # reorder the shift's preference_score (if taking times taken, it's not needed) - evalute_shift_preference()
            week_shift_weights = {week_shift: week_shift_weight for week_shift, week_shift_weight in week_shift_weights.items() if week_shift in week_shifts}

        employee.next_week_shifts += chosen_shifts

    def _remove_illegal_shifts(self, chosen_shifts: List[Shift], week_shift_candidates: List[Shift], week_start: datetime) -> List[Shift]:
        filtered_shifts = week_shift_candidates.copy()
        new_shift = chosen_shifts[-1]
        best_shift_start = new_shift.start_time
        best_shift_end = new_shift.end_times

        for week_shift_candidate in week_shift_candidates:
            shift_candidate = Shift(
                week_start + timedelta(days=week_shift_candidate.weekday, hours=week_shift_candidate.start_time),
                week_start + timedelta(days=week_shift_candidate.weekday, 
                                       hours=week_shift_candidate.start_time + week_shift_candidate.full_duration / 60
                                       ),
                week_shift_candidate.duration,
            )

            pend_shift_start = shift_candidate.start_time
            pend_shift_end = shift_candidate.endTime

            start_diff = abs(best_shift_end - pend_shift_start)
            endDiff = abs(best_shift_start - pend_shift_end)

            start_hour_diff = start_diff.days * 24 + start_diff.seconds // 3600
            end_hour_diff = endDiff.days * 24 + endDiff.seconds // 3600
            if (start_hour_diff < 12 or end_hour_diff < 12) or (pend_shift_start == best_shift_start and pend_shift_end == best_shift_end):
                filtered_shifts.remove(week_shift_candidate)

        return filtered_shifts

    def _get_weighted_week_shift_counts(self, shifts: List[WeekShift], week_start: datetime):
        weighted_week_shifts = {}
        for shift in shifts:
            week_shift = WeekShift(shift.start_time.weekday(), shift.start_time.hour, shift.duration, (shift.endTime - shift.start_time).seconds / 60)
            if week_shift not in weighted_week_shifts.keys():
                weighted_week_shifts[week_shift] = self._get_weighed_shift(week_shift, shifts, week_start)
        return dict(sorted(weighted_week_shifts.items(), key=lambda item: item[1], reverse=True))

    def _get_weighed_shift(self, week_shift: WeekShift, shifts: List[Shift], week_start: datetime) -> float:
        # TODO implement "shift_frequency" function here
        return sum([self._timespan_weight(week_start - shift.start_time) for shift in shifts if week_shift.matches_shift(shift)])

    def _timespan_weight(self, timediff):
        w = float(abs(timediff.days)) / 7.0
        return math.exp(-w)
