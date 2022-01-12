import json
from flask import Flask, request
from src.modules.api_mapper import *

from src.shift_generator import ShiftGenerator

app = Flask(__name__)

shiftGenerator = ShiftGenerator()

@app.route("/")
def hello():
    return json.dumps('Hi from Team Schedule AI!')


@app.route("/generate", methods=["POST"])
def generate():
    employees, weekStart = map_request_to_classes(request.json)
    shiftGenerator.create_weekly_schedule(employees, weekStart)  

    return json.dumps(employees[0].toJson())

    #return json.dumps(request.json)
