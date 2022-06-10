from datetime import datetime
from typing import List

from src.models.employee import Employee
from src.modules.schedule_generator.shift_frequency_generator.shift_frequency_generator import ShiftFrequencyGenerator


class ScheduleManager:
    def __init__(self):
        self.predictor = ShiftFrequencyGenerator()

    def generate_schedule(
        self, employees: List[Employee], weekStart: datetime, weeksAheadCount: int, availableSlots=None
    ):
        self.predictor.generate_schedule(employees, weekStart, weeksAheadCount, availableSlots)
