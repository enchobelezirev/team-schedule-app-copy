from typing import List
from src.models.Shift import Shift

class Employee:
    def __init__(self, uid: str, weeklyHours: int, pastShifts: List[Shift]):
        self.uid = uid
        self.weeklyHours = weeklyHours
        self.pastShifts = pastShifts
        self.nextWeekShifts = []

    def toJson(self):
        result = '{'
        result += f'"UserId": "{self.uid}",'
        result += '"NextWeekShifts": ['

        shift_jsons = []
        for shift in self.nextWeekShifts:
            shift_jsons.append(shift.toJson())
        result += ','.join(shift_jsons)

        result += ']}'
            
        return result