from src.models.shift import Shift


class WeekShift:
    def __init__(self, weekday, startTime, duration, fullDuration):
        self.weekday = weekday
        self.startTime = startTime
        self.duration = duration
        self.fullDuration = fullDuration

    def __eq__(self, other):
        if isinstance(other, WeekShift):
            return (
                self.weekday == other.weekday
                and self.startTime == other.startTime
                and self.duration == other.duration
                and self.fullDuration == other.fullDuration
            )
        return False

    def __hash__(self):
        return hash((self.weekday, self.startTime, self.duration, self.fullDuration))

    def matches_shift(self, shift: Shift):
        return self.weekday == shift.startTime.weekday() and self.startTime == shift.startTime.hour and self.duration == shift.duration
