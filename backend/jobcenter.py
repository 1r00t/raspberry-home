from jobs.speedtest_job import SpeedTest
from threading import Event, Thread
from time import sleep


class Jobs():
    def __init__(self, *args, **kwargs):
        self.exit = Event()
        self.exit.set()
        self.worker = None

    def speedtest(self, minutes=2):
        speedtest = SpeedTest()

        while not self.exit.is_set():
            speedtest.run()
            speedtest.write_log()

            self.exit.wait(minutes * 60)

    def speedtest_start(self, minutes):
        self.speedtest_stop()
        self.exit = Event()  # set started
        self.worker = Thread(target=self.speedtest, args=[minutes])
        self.worker.start()

    def speedtest_stop(self):
        if self.exit.is_set():
            if not self.worker:
                return
            while self.worker.is_alive():
                # wait until task is finished
                sleep(0.1)
        else:
            self.exit.set()

    def speedtest_running(self):
        return not self.exit.is_set()
