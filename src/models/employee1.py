from typing import List

from src.models.shift import Shift


class Employee:
    def __init__(self, uid: str, weeklyHours: int, pastShifts: List[Shift]):
        self.uid = uid
        self.weeklyHours = weeklyHours
        self.pastShifts = pastShifts
        self.nextWeekShifts = []

    def get_last_shift(self):
        shifts = self.pastShifts + self.nextWeekShifts
        shifts.sort(key=lambda x: x.endTime)
        return shifts[-1]
