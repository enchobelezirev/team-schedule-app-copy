from datetime import datetime
from typing import List

from src.models.employee import Employee


class Schedule:
    def __init__(self, managerId: str, weekStart: datetime, weeksAheadCount: int, employees: List[Employee]):
        self.managerId = managerId
        self.weekStart = weekStart
        self.weeksAheadCount = weeksAheadCount
        self.employees = employees
