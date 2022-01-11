from typing import List
from datetime import datetime

from src.modules.ShiftFrequencyPredictor.ShiftFrequencyPredictor import ShiftFrequencyPredictor
from src.models.Employee import Employee

class ShiftGenerator():
    def __init__(self):
        self.predictor = ShiftFrequencyPredictor()

    def create_weekly_schedule(self, employees: List[Employee], weekStart: datetime, availableSlots = None):
        self.predictor.create_weekly_schedule(employees, weekStart, availableSlots)