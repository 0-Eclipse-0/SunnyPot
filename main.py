# SunnyPot Main
import argparse
from src.Server import Server
from src.Message import Message
import signal
from src.Config import Config

if __name__ == '__main__':
    # Init argparse object
    parser = argparse.ArgumentParser(
        prog='SunnyPot',
        description='Configurable HoneyPot for small scale usage')

    # Arguments List
    parser.add_argument('--config', action='store_true', dest='config')
    parser.add_argument('--generate', action='store_true', dest='generate')
    parser.add_argument('--read', action='store_true', dest='read')
    parser.add_argument('--host', dest='host',
                        help='Host address for HoneyPot to run on')
    parser.add_argument('--port', dest='port', default=22,
                        help='Selected port to run HoneyPot on, default: 22')
    parser.add_argument('--database', dest='database',
                        help='Selected database file, default: log.db')

    args = parser.parse_args()

    try:
        # Mode selector
        if args.read == True:  # TODO add read
            pass
        else:
            # Determine where to retrieve data
            if args.config:
                host, port, database = Config.parse()
                s = Server(host, port, database)
            else:
                if args.generate: # Gen config if necessary
                    Config.generate(args.host, args.port, args.database)

                s = Server(args.host, args.port, args.database)

            s.build()
            s.listen()

    except KeyboardInterrupt: # Clean exit
        Message.abort("Shutting down HoneyPot...")


