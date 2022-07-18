import json
from src.models.schedule import Schedule
from src.modules.api_mapper.api_mapper import map_request_to_classes

ONE_EMPLOYEE_SCHEDULE_PATH = "test/data/sample_files/manager_single_employee.json"


def get_schedule_with_a_single_employee() -> Schedule:
    with open(ONE_EMPLOYEE_SCHEDULE_PATH, "r", encoding="utf-8") as file:
        sample_json = json.load(file)

    return map_request_to_classes(sample_json)
