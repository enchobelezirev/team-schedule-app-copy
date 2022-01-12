import json
from src.shift_generator import ShiftGenerator
from src.modules.api_mapper import *

shiftGenerator = ShiftGenerator()

def generate_sample(sample_path: str) -> str:
    f = open(sample_path)
    sample_json = json.load(f)

    employees, weekStart = map_request_to_classes(sample_json)
    shiftGenerator.create_weekly_schedule(employees, weekStart)  

    return json.dumps(employees[0].toJson())

sample_json_path = 'sample_data/single_employee.json'
print(generate_sample(sample_json_path))