from datetime import datetime

from src.models.employee import Employee
from src.models.schedule import Schedule
from src.models.shift import Shift


def map_request_to_classes(request_json: str) -> Schedule:
    manager_id = request_json["ManagerId"]
    # The month from the input is in range [0, 11]. E.g. 0: January, 11: December.
    week_start = datetime(
        request_json["MondayOfWeekToGenerateFor"]["year"],
        request_json["MondayOfWeekToGenerateFor"]["month"] + 1,
        request_json["MondayOfWeekToGenerateFor"]["date"],
    )
    weeks_to_predict_count = request_json["WeeksToPredictAheadCount"]

    employees = []
    for employee in request_json["Employees"]:
        curr_uid = employee["UserId"]
        curr_weekly_hours = int(employee["Standard Weekly Hours"])

        curr_shifts = []
        for shift in employee["PastShifts"]:
            curr_shift_start = datetime(
                shift["startDate"]["year"],
                shift["startDate"]["month"] + 1,
                shift["startDate"]["date"],
                shift["startTime"]["hours"],
                shift["startTime"]["minutes"],
            )
            curr_shift_end = datetime(
                shift["endDate"]["year"],
                shift["startDate"]["month"] + 1,
                shift["endDate"]["date"],
                shift["endTime"]["hours"],
                shift["endTime"]["minutes"],
            )
            curr_shift_duration = shift["duration"]

            new_shift = Shift(curr_shift_start, curr_shift_end, curr_shift_duration)
            curr_shifts.append(new_shift)

        new_employee = Employee(curr_uid, curr_weekly_hours, curr_shifts)
        employees.append(new_employee)

    return Schedule(manager_id, week_start, weeks_to_predict_count, employees)
