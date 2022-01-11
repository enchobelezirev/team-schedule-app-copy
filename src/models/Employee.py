from typing import List
from src.models.Shift import Shift

class Employee:
    def __init__(self, uid: str, weeklyHours: int, pastShifts: List[Shift]):
        self.uid = uid
        self.weeklyHours = weeklyHours
        self.pastShifts = pastShifts
        self.nextWeekShifts = []

    def toJson(self):
        result = ''
        
        for shift in self.nextWeekShifts:
            result += shift.toJson()
            
        return result