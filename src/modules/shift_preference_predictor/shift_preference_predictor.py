from typing import List
from datetime import datetime

from src.models.shift import Shift

class ShiftPreferencePredictor():
    def __init__(self):
        pass

    def get_most_prefered_shifts(self, shifts: List[Shift], week_start: datetime) -> Shift:
        pass

    def get_top_n_prefered_shifts(self, shifts: List[Shift], week_start: datetime) -> List[Shift]:
        pass
