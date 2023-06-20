# Server handler

import socket
from time import sleep
from src.Log import Log
from src.Message import Message

class Server:
    def __init__(self, host, port, database):
        self.host = host
        self.port = int(port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log = Log(database)

    # Start honeypot
    def build(self):
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        if self.host == None:
            self.host = socket.gethostbyname(socket.gethostname())

            if self.host == "127.0.0.1":
                Message.abort("Error resolving hostname, please enter manually...")

        # Attempt to make server
        Message.log("Attempting to bind server to port...")

        try:
            self.server.bind((self.host, self.port))
        except Exception as e:
            Message.abort(e)

        Message.log("Server started on %s:%i..." % (self.host, self.port))

        self.server.listen(5)

    def listen(self):
        Message.log("Server listening on %s:%s..." % (self.host, self.port))

        # Accept connections
        while True:
            sleep(1)
            attacker, (clientHost, clientPort) = self.server.accept()

            self.log.write(clientHost)


