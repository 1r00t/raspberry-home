import speedtest
from datetime import datetime
import os
from csv import DictWriter
import pathlib


BASE_DIR = pathlib.Path(__file__).parent.absolute()
LOG_CSV = os.path.join(BASE_DIR, "connection_log.csv")


class SpeedTest():
    def __init__(self, servers=[], threads=None):
        self.servers = servers
        self.threads = threads
        self.time = None
        self.result_json = None

    def run(self):
        self.time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        try:
            self.st = speedtest.Speedtest()
        except speedtest.ConfigRetrievalError or speedtest.ShareResultsConnectFailure:
            self.no_connection()
            return

        self.st.get_servers(self.servers)
        self.st.get_best_server()
        self.st.download(threads=self.threads)
        self.st.upload(threads=self.threads)
        self.st.results.share()

        result = self.st.results.dict()

        self.result_json = {
            "time": self.time,
            "connected": True,
            "download": result["download"],
            "upload": result["upload"],
            "ping": result["ping"],
            "server": result["server"]["url"]
        }

    def no_connection(self):
        self.result_json = {
            "time": self.time,
            "connected": False,
            "download": 0.0,
            "upload": 0.0,
            "ping": 0.0,
            "server": "",
        }

    def write_log(self):

        csv_exists = os.path.isfile(LOG_CSV)

        with open(LOG_CSV, "a") as csvfile:
            fieldnames = ["time", "connected", "download", "upload", "ping", "server"]
            writer = DictWriter(csvfile, fieldnames)
            if not csv_exists:
                writer.writeheader()
            writer.writerow(self.result_json)


if __name__ == "__main__":
    print("Initializing ...")
    speed_test = SpeedTest()

    print("Running ...")
    speed_test.run()

    print("Writing log file ...")
    speed_test.write_log()

    print("Done!")
