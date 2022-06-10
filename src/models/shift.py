from datetime import timedelta


class Shift:
    def __init__(self, start_time, end_time, duration):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration

    @classmethod
    def from_weekshift(cls, week_shift, week_start):
        return cls(
            week_start + timedelta(days=week_shift.weekday, hours=week_shift.start_time),
            week_start + timedelta(days=week_shift.weekday, hours=week_shift.start_time + week_shift.full_duration / 60),
            week_shift.duration,
        )

    def __hash__(self):
        return hash((self.start_time, self.end_time, self.duration))

    def __eq__(self, other) -> bool:
        return self.start_time == other.start_time and self.end_time == other.end_time and self.duration == other.duration

    def __gt__(self, other):
        return self.start_time > other.start_time

    def equals(self, other) -> bool:
        return self.start_time == other.start_time and self.end_time == other.end_time and self.duration == other.duration

    def length(self):
        shiftLength = self.end_time - self.start_time
        return shiftLength if shiftLength > timedelta(0) else timedelta(0)

    def __get_matching_time_with_shift(self, other):
        # if the minimum end time is before the maximum start time, then there is an intersection
        matchingTime = min([self.end_time, other.end_time]) - max([self.start_time, other.start_time])
        return max(timedelta(0), matchingTime)

    def get_matching_time_with_shifts(self, shifts):
        totalMatchingTime = sum(map(lambda shift: self.__get_matching_time_with_shift(shift), shifts), timedelta(0))
        return totalMatchingTime

    def display_values(self):
        print(f" Start: {self.start_time}")
        print(f" End: {self.end_time}")
        print(f" Duration: {self.duration}")

    def rest_time(self, shift):
        return min(abs((self.end_time - shift.start_time).seconds / 3600 + (self.end_time - shift.start_time).days * 24),
        abs((shift.end_time - self.start_time).seconds / 3600 + (shift.end_time - self.start_time).days + 24))
