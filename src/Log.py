# Logger class
from datetime import datetime
from src.Message import Message
import sqlite3

class Log:
    def __init__(self, database):
        if database == None: # Determine custom database
            database = "log.db"

        self.logger = sqlite3.connect(database)
        self.logger.execute("CREATE TABLE if NOT EXISTS INTRUSIONS (attempt_ip TEXT, "
                            "attempt_time TEXT, "
                            "attempt_date TEXT)")

    def read(self):
        pass

    def write(self, host):
        # Timestamps
        time = datetime.now().strftime("%H:%M:%S")
        date = datetime.now().strftime("%m-%d-%y")

        # Outputs
        Message.intrusion("Host %s attempted to connect @ %s on %s" % (host, date, time))
        self.logger.execute("INSERT INTO INTRUSIONS (attempt_ip, attempt_time, attempt_date) VALUES ('%s', '%s', '%s' )" % (host, time, date))
