import json
from flask import Flask, request
from src.modules.api_mapper import *

from src.shift_generator import ShiftGenerator
from src.models.encoders.JSONEncoder import JSONEncoder

app = Flask(__name__)

shiftGenerator = ShiftGenerator()

@app.route("/")
def hello():
    return json.dumps('Hello from TeamSchedule AI!')


@app.route("/generate", methods=["POST"])
def generate():
    schedule = map_request_to_classes(request.json)
    shiftGenerator.generate_schedule(schedule.employees, schedule.weekStart, schedule.weeksAheadCount)  

    return json.dumps(schedule, cls=JSONEncoder)
