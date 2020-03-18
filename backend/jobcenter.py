from jobs.speedtest_job import SpeedTest
import threading
from time import sleep


class Jobs():
    def __init__(self, *args, **kwargs):
        self.workers = {
            "speedtest": {
                "thread": threading.Thread(target=self.speedtest),
                "running": False
            }
        }

    def speedtest(self, minutes=2):
        while self.workers["speedtest"]["running"]:
            speedtest = SpeedTest()
            speedtest.run()
            speedtest.write_log()

            sleep(minutes * 60)

    def speedtest_start(self, minutes):
        if self.workers["speedtest"]["running"]:
            return

        self.workers["speedtest"]["running"] = True
        self.workers["speedtest"]["thread"].args = [minutes]
        self.workers["speedtest"]["thread"].start()

    def speedtest_stop(self):
        if not self.workers["speedtest"]["running"]:
            return

        self.workers["speedtest"]["running"] = False
        self.workers["speedtest"]["thread"].join()

    def speedtest_running(self):
        return self.workers["speedtest"]["running"]
