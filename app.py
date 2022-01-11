from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

from shift_app.shift_generator import ShiftGenerator

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

shiftGenerator = ShiftGenerator()

@app.route("/")
@cross_origin()
def hello():
    return json.dumps('Hi from TeamSchedule AI!')


@app.route("/generate", methods=["POST"])
@cross_origin()
def generate():

    #TODO: Add real
    # employees, weekStart = map_request_to_classes(request)
    # create_weekly_schedule(employees, weekStart)   
    # return json.dumps(employees[0].toJson())

    return json.dumps(request.json)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9002, app)