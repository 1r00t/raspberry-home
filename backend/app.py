from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import os

from crontab import CronTab

app = Flask(__name__)
api = Api(app)


# CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)


class SpeedTest(Resource):
    def __init__(self):
        self.job = None
        self.cron = CronTab(user=True)
        command = os.environ["SPEEDTEST_CMD"]

        for job in self.cron:
            if job.comment == "speedtest":
                self.job = job
        if not self.job:
            self.job = self.cron.new(command=command, comment="speedtest")
            self.job.minute.every(2)
            self.job.enable(False)
            self.cron.write()

    def get(self):
        return {"is_enabled": self.job.is_enabled()}

    def post(self):
        data = request.get_json()
        if data.get("job") == "start":
            self.job.enable()
            if data.get("minute"):
                self.job.minute.every(data.get("minute"))
            self.cron.write()
            return {"is_enabled": True}
        elif data.get("job") == "stop":
            self.job.enable(False)
            self.cron.write()
            return {"is_enabled": False}
        return False


api.add_resource(SpeedTest, "/speedtest")


if __name__ == "__main__":
    app.run(debug=True)
