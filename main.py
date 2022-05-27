import json
from src.models.JSONEncoder import JSONEncoder
from src.shift_generator import ShiftGenerator
from src.modules.api_mapper import *

shiftGenerator = ShiftGenerator()

def generate_sample(sample_path: str) -> str:
    f = open(sample_path)
    sample_json = json.load(f)

    schedule = map_request_to_classes(sample_json)
    shiftGenerator.generate_schedule(schedule.employees, schedule.weekStart, 4)  

    _show_pretty_schedule(schedule)

    return json.dumps(schedule, cls=JSONEncoder)

def _show_pretty_schedule(schedule: Schedule):
    for employee in schedule.employees:
        print('------- Employee', employee.uid)
        for shift in sorted(employee.nextWeekShifts):
            print(shift.startTime, '-', shift.endTime)

sample_json_path = 'sample_data/single_employee.json'
print(generate_sample(sample_json_path).replace('', ''))
