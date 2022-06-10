from typing import List

from src.models.shift import Shift


class Employee:
    def __init__(self, uid: str, weekly_hours: int, past_shifts: List[Shift]):
        self.uid = uid
        self.weekly_hours = weekly_hours
        self.past_shifts = past_shifts
        self.next_week_shifts = []

    def get_last_shift(self):
        shifts = self.past_shifts + self.next_week_shifts
        shifts.sort(key=lambda x: x.endTime)
        return shifts[-1]
