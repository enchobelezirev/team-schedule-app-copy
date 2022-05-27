from datetime import datetime

from src.models.employee import Employee
from src.models.schedule import Schedule
from src.models.shift import Shift


def map_request_to_classes(requestJson: str) -> Schedule:
    managerId = requestJson["ManagerId"]
    # The month from the input is in range [0, 11]. E.g. 0: January, 11: December.
    weekStart = datetime(
        requestJson["MondayOfWeekToGenerateFor"]["year"],
        requestJson["MondayOfWeekToGenerateFor"]["month"] + 1,
        requestJson["MondayOfWeekToGenerateFor"]["date"],
    )
    weeksToPredictCount = requestJson["WeeksToPredictAheadCount"]

    employees = []
    for employee in requestJson["Employees"]:
        currUid = employee["UserId"]
        currWeeklyHours = int(employee["Standard Weekly Hours"])

        currShifts = []
        for shift in employee["PastShifts"]:
            currShiftStart = datetime(
                shift["startDate"]["year"],
                shift["startDate"]["month"] + 1,
                shift["startDate"]["date"],
                shift["startTime"]["hours"],
                shift["startTime"]["minutes"],
            )
            currShiftEnd = datetime(
                shift["endDate"]["year"],
                shift["startDate"]["month"] + 1,
                shift["endDate"]["date"],
                shift["endTime"]["hours"],
                shift["endTime"]["minutes"],
            )
            currShiftDuration = shift["duration"]

            newShift = Shift(currShiftStart, currShiftEnd, currShiftDuration)
            currShifts.append(newShift)

        newEmployee = Employee(currUid, currWeeklyHours, currShifts)
        employees.append(newEmployee)

    return Schedule(managerId, weekStart, weeksToPredictCount, employees)
