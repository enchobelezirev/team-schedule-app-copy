from typing import List
from datetime import datetime

from src.models.Employee import Employee

class Schedule:
    def __init__(self, managerId: str, weekStart: datetime, weeksAheadCount: int, employees: List[Employee]):
        self.managerId = managerId
        self.weekStart = weekStart
        self.weeksAheadCount = weeksAheadCount
        self.employees = employees

