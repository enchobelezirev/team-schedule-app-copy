from src.models.shift import Shift


class WeekShift:
    def __init__(self, weekday, start_time, duration, full_duration):
        self.weekday = weekday
        self.start_time = start_time
        self.duration = duration
        self.full_duration = full_duration

    def __eq__(self, other):
        if isinstance(other, WeekShift):
            return (
                self.weekday == other.weekday
                and self.start_time == other.start_time
                and self.duration == other.duration
                and self.full_duration == other.full_duration
            )
        return False

    def __hash__(self):
        return hash((self.weekday, self.start_time, self.duration, self.full_duration))

    def matches_shift(self, shift: Shift):
        return (
            self.weekday == shift.start_time.weekday()
            and self.start_time == shift.start_time.hour
            and self.duration == shift.duration
        )
