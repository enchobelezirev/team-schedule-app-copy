from flask import Flask, request
import json

from shift_app.shift_generator import ShiftGenerator

app = Flask(__name__)

shiftGenerator = ShiftGenerator()

@app.route("/")
def hello():
    return json.dumps('Hi from TeamSchedule AI!')


@app.route("/generate", methods=["POST"])
def generate():

    #TODO: Add real
    # employees, weekStart = map_request_to_classes(request)
    # create_weekly_schedule(employees, weekStart)   
    # return json.dumps(employees[0].toJson())

    return json.dumps(request.json)
