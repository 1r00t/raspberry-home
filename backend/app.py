from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

from jobcenter import Jobs

import os
import csv


app = Flask(__name__)
CORS(app)
api = Api(app)

jobs = Jobs()


class SpeedTest(Resource):
    def __init__(self):
        self.connection_log = os.environ.get("SPEEDTEST_CSV_FILE")

    def get(self):
        speed_data = self._get_speed_data()
        running = jobs.speedtest_running()
        return jsonify({
            "is_enabled": running,
            "speed_data": speed_data
        })

    def post(self):
        data = request.get_json()

        # start speedtest
        if data.get("job") == "start":
            minutes = data.get("minutes", 2)
            jobs.speedtest_start(minutes)

            return jsonify({
                "is_enabled": jobs.speedtest_running()
            })

        # stop speedtest
        elif data.get("job") == "stop":
            jobs.speedtest_stop()

            return jsonify({
                "is_enabled": jobs.speedtest_running()
            })

        return False

    def _get_speed_data(self):
        speed_data = []
        if os.path.exists(self.connection_log):
            with open(self.connection_log, newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    speed_data.append(row)
        return speed_data


api.add_resource(SpeedTest, "/speedtest")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
