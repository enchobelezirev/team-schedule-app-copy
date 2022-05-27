from datetime import timedelta

class Shift:
    def __init__(self, startTime, endTime, duration):
        self.startTime = startTime
        self.endTime = endTime
        self.duration = duration
    
    def __hash__(self):
        return hash((self.startTime, self.endTime, self.duration))
        
    def __eq__(self, other) -> bool:
        return self.startTime == other.startTime and self.endTime == other.endTime and self.duration == other.duration
    
    def __gt__(self,other):
        return self.startTime > other.startTime
        
    def equals(self, other) -> bool:
        return self.startTime == other.startTime and self.endTime == other.endTime and self.duration == other.duration
        
    def length(self):
        shiftLength = self.endTime - self.startTime
        return shiftLength if shiftLength > timedelta(0) else timedelta(0)
        
    def __get_matching_time_with_shift(self, other):
        # if the minimum end time is before the maximum start time, then there is an intersection
        matchingTime = min([self.endTime, other.endTime]) - max([self.startTime, other.startTime])
        return max(timedelta(0), matchingTime)
    
    def get_matching_time_with_shifts(self, shifts):
        totalMatchingTime = sum(map(lambda shift: self.__get_matching_time_with_shift(shift), shifts), timedelta(0))
        return totalMatchingTime
    
    def display_values(self):
        print(f' Start: {self.startTime}')
        print(f' End: {self.endTime}')
        print(f' Duration: {self.duration}')
