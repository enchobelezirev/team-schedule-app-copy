from datetime import datetime
from typing import List

from src.models.employee import Employee


class Schedule:
    def __init__(self, manager_id: str, week_start: datetime, weeks_ahead_count: int, employees: List[Employee]):
        self.manager_id = manager_id
        self.week_start = week_start
        self.weeks_ahead_count = weeks_ahead_count
        self.employees = employees
