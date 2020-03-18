from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

from jobcenter import Jobs


app = Flask(__name__)
CORS(app)
api = Api(app)

jobs = Jobs()


class SpeedTest(Resource):
    def get(self):
        running = jobs.speedtest_running()
        return jsonify({
            "is_enabled": running
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


api.add_resource(SpeedTest, "/speedtest")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
