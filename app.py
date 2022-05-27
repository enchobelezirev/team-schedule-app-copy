import json

from flask import Flask, request

from src.models.encoders.json_encoder import JSONEncoder
from src.modules.api_mapper.api_mapper import map_request_to_classes
from src.modules.schedule_manager import ScheduleManager

app = Flask(__name__)

shiftGenerator = ScheduleManager()


@app.route("/")
def hello():
    return json.dumps("Hello from TeamSchedule AI!")


@app.route("/generate", methods=["POST"])
def generate():
    schedule = map_request_to_classes(request.json)
    shiftGenerator.generate_schedule(schedule.employees, schedule.weekStart, schedule.weeksAheadCount)

    return json.dumps(schedule, cls=JSONEncoder)
