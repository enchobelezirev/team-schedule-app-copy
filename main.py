import json
from src.shift_generator import ShiftGenerator
from src.modules.api_mapper import *

shiftGenerator = ShiftGenerator()

def generate_sample(sample_path: str) -> str:
    f = open(sample_path)
    sample_json = json.load(f)

    schedule = map_request_to_classes(sample_json)
    shiftGenerator.create_weekly_schedule(schedule.employees, schedule.weekStart)  

    result = json.loads(schedule.toJson())
    return json.dumps(result)

sample_json_path = 'sample_data/single_employee.json'
print(generate_sample(sample_json_path).replace('', ''))
