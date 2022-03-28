from typing import List
from datetime import datetime

from src.modules.ShiftFrequencyPredictor.ShiftFrequencyPredictor import ShiftFrequencyPredictor
from src.models.Employee import Employee

class ShiftGenerator():
    def __init__(self):
        self.predictor = ShiftFrequencyPredictor()

    def generate_schedule(self, employees: List[Employee], weekStart: datetime, weeksAheadCount: int, availableSlots = None):
        self.predictor.generate_schedule(employees, weekStart, weeksAheadCount, availableSlots)