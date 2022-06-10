from src.models.employee import Employee
from src.models.shift import Shift
from src.modules.utils.constants import REST_BETWEEN_SHIFTS


class ShiftRestrictionManager:
    def __init__(self):
        pass

    def is_shift_allowed(self, employee: Employee, shift: Shift) -> bool:
        return self.__has_legal_rest_between_shifts(employee, shift)

    def __has_legal_rest_between_shifts(self, employee: Employee, shift: Shift) -> bool:
        shifts = employee.past_shifts + employee.next_week_shifts + [shift]
        shifts.sort(key=lambda shift: shift.end_time)
        shift_index = shifts.index(shift)
        if shift_index > 0:
            prev_shift = shifts[shift_index - 1]
            if shift.rest_time(prev_shift) < REST_BETWEEN_SHIFTS:
                return False
        if shift_index < len(shifts) - 1:
            next_shift = shifts[shift_index + 1]
            if shift.rest_time(next_shift) < REST_BETWEEN_SHIFTS:
                return False

        return True
