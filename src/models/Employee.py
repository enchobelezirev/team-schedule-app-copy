from typing import List
from src.models.shift import Shift

class Employee:
    def __init__(self, uid: str, weeklyHours: int, pastShifts: List[Shift]):
        self.uid = uid
        self.weeklyHours = weeklyHours
        self.pastShifts = pastShifts
        self.nextWeekShifts = []
