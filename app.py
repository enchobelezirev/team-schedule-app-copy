import json

from flask import Flask, request
from flask import jsonify
from flask_api import status


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
    try:
        schedule = map_request_to_classes(request.json)
    except Exception:
        return {"error": "Schedule is missing or ca not be mapped"}, status.HTTP_400_BAD_REQUEST, ""

    shiftGenerator.generate_schedule(schedule.employees, schedule.week_start, schedule.weeks_ahead_count)
    return jsonify(json.dumps(schedule, cls=JSONEncoder))
