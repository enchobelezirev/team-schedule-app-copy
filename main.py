import json

from src.models.encoders.json_encoder import JSONEncoder
from src.models.schedule import Schedule
from src.modules.api_mapper.api_mapper import map_request_to_classes
from src.modules.schedule_manager import ScheduleManager
from src.modules.utils.visualization import visualize_schedule

schedule_manager = ScheduleManager()


def generate_sample(sample_path: str) -> str:
    with open(sample_path, "r", encoding="utf-8") as file:
        sample_json = json.load(file)

    schedule = map_request_to_classes(sample_json)
    schedule_manager.generate_schedule(schedule.employees, schedule.week_start, 4)

    _show_pretty_schedule(schedule)
    visualize_schedule(schedule)

    return json.dumps(schedule, cls=JSONEncoder)


def _show_pretty_schedule(schedule: Schedule):
    for employee in schedule.employees:
        print("------- Employee", employee.uid)
        for shift in sorted(employee.next_week_shifts):
            print(shift.start_time, "-", shift.end_time)


sample_json_path = "sample_data/two_employees.json"
print(generate_sample(sample_json_path).replace("", ""))
