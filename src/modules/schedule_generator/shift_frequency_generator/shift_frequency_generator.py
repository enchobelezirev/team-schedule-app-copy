import math
from datetime import datetime, timedelta
from typing import List

from src.models.employee import Employee
from src.models.shift import Shift
from src.modules.schedule_generator.shift_frequency_generator.models.week_shift import WeekShift


class ShiftFrequencyGenerator:
    def __init__(self):
        pass

    def generate_schedule(
        self, employees: List[Employee], weekStart: datetime, weeksAheadCount: int, availableSlots=None
    ):
        """
        Generate the shifts for N weeks ahead.
        """
        for i in range(weeksAheadCount):
            self.create_weekly_schedule(employees, weekStart)
            weekStart += timedelta(days=7)

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

    def _assign_shifts_given_employee(self, employee: Employee, weekStart: datetime):
        """
        Implementation of the simples case of assigning a single employee.
        """
        # Here we can add any other of the ideas we discussed
        return self._infinite_potential_idea(employee, weekStart)

    def _infinite_potential_idea(self, employee: Employee, weekStart: datetime) -> List[Shift]:
        # shiftCandidates = Take all employee possible shifts
        employeeShifts = employee.pastShifts + employee.nextWeekShifts
        weekshiftWeights = self._get_weighted_week_shift_counts(employeeShifts, weekStart)
        weekshifts = set([weekshift for weekshift, weekshiftWeight in weekshiftWeights.items()])
        currentHours = 0
        chosenShifts = []

        # while current_hours < weekly_hours
        while currentHours < employee.weeklyHours and len(weekshiftWeights) > 0:
            # pick the top slot
            topWeeklyShift = next(iter(weekshiftWeights))
            topShift = Shift(
                weekStart + timedelta(days=topWeeklyShift.weekday, hours=topWeeklyShift.startTime),
                weekStart
                + timedelta(
                    days=topWeeklyShift.weekday, hours=topWeeklyShift.startTime + topWeeklyShift.fullDuration / 60
                ),
                topWeeklyShift.duration,
            )
            currentHours += topShift.duration / 60
            chosenShifts.append(topShift)
            # remove illegal shifts according to filled ones
            weekshifts = set(self._remove_illegal_shifts(chosenShifts, weekshifts, weekStart))
            # reorder the shift's preference_score (if taking times taken, it's not needed) - evalute_shift_preference()
            weekshiftWeights = {
                weekshift: weekshiftWeight
                for weekshift, weekshiftWeight in weekshiftWeights.items()
                if weekshift in weekshifts
            }

        employee.nextWeekShifts += chosenShifts

    def _remove_illegal_shifts(
        self, chosenShifts: List[Shift], weekshiftCandidates: List[Shift], weekStart: datetime
    ) -> List[Shift]:
        filteredShifts = weekshiftCandidates.copy()
        newShift = chosenShifts[-1]
        bestShiftStart = newShift.startTime
        bestShiftEnd = newShift.endTime

        for weekshiftCandidate in weekshiftCandidates:
            shiftCandidate = Shift(
                weekStart + timedelta(days=weekshiftCandidate.weekday, hours=weekshiftCandidate.startTime),
                weekStart
                + timedelta(
                    days=weekshiftCandidate.weekday,
                    hours=weekshiftCandidate.startTime + weekshiftCandidate.fullDuration / 60,
                ),
                weekshiftCandidate.duration,
            )

            pendShiftStart = shiftCandidate.startTime
            pendShiftEnd = shiftCandidate.endTime

            startDiff = abs(bestShiftEnd - pendShiftStart)
            endDiff = abs(bestShiftStart - pendShiftEnd)

            startHourDiff = startDiff.days * 24 + startDiff.seconds // 3600
            endHourDiff = endDiff.days * 24 + endDiff.seconds // 3600
            if (startHourDiff < 12 or endHourDiff < 12) or (
                pendShiftStart == bestShiftStart and pendShiftEnd == bestShiftEnd
            ):
                filteredShifts.remove(weekshiftCandidate)

        return filteredShifts

    def _get_weighted_week_shift_counts(self, shifts: List[WeekShift], weekStart: datetime):
        weightedWeekshifts = {}
        for shift in shifts:
            weekshift = WeekShift(
                shift.startTime.weekday(),
                shift.startTime.hour,
                shift.duration,
                (shift.endTime - shift.startTime).seconds / 60,
            )
            if weekshift not in weightedWeekshifts.keys():
                weightedWeekshifts[weekshift] = self._get_weighed_shift(weekshift, shifts, weekStart)
        return dict(sorted(weightedWeekshifts.items(), key=lambda item: item[1], reverse=True))

    def _get_weighed_shift(self, weekshift: WeekShift, shifts: List[Shift], weekStart: datetime) -> float:
        # TODO implement "shift_frequency" function here
        return sum(
            [self._timespan_weight(weekStart - shift.startTime) for shift in shifts if weekshift.matches_shift(shift)]
        )

    def _timespan_weight(self, timediff):
        w = float(abs(timediff.days)) / 7.0
        return math.exp(-w)
