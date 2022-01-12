from datetime import datetime

from src.models.Schedule import Schedule
from src.models.Employee import Employee
from src.models.Shift import Shift

def map_request_to_classes(requestJson: str) -> Schedule:
    managerId = requestJson['ManagerId']
    weekStart = datetime(requestJson['MondayOfWeekToGenerateFor']['year'], requestJson['MondayOfWeekToGenerateFor']['month'], requestJson['MondayOfWeekToGenerateFor']['date'])
    
    employees = []
    for employee in requestJson['Employees']:
        currUid = employee['UserId']
        currWeeklyHours = int(employee['Standard Weekly Hours'])
        
        currShifts = []
        for shift in employee['PastShifts']:
            currShiftStart = datetime(shift['startDate']['year'], shift['startDate']['month'], shift['startDate']['date'], shift['startTime']['hours'], shift['startTime']['minutes'])
            currShiftEnd = datetime(shift['endDate']['year'], shift['endDate']['month'], shift['endDate']['date'], shift['endTime']['hours'], shift['endTime']['minutes'])
            currShiftDuration = shift['duration']
            
            newShift = Shift(currShiftStart, currShiftEnd, currShiftDuration)
            currShifts.append(newShift)
        
        newEmployee = Employee(currUid, currWeeklyHours, currShifts)
        employees.append(newEmployee)
    
    return Schedule(managerId, weekStart, employees)
