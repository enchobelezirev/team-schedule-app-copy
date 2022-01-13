import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
from src.modules.api_mapper import *

from src.shift_generator import ShiftGenerator

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

shiftGenerator = ShiftGenerator()

@app.route("/")
@cross_origin()
def hello():
    return json.dumps('Hello from TeamSchedule AI!')


@app.route("/generate", methods=["POST"])
@cross_origin()
def generate():
    schedule = map_request_to_classes(request.json)
    shiftGenerator.create_weekly_schedule(schedule.employees, schedule.weekStart)  

    result = json.loads(schedule.toJson())
    return json.dumps(result)
