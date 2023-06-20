# Config handler

import re

class Config:
    def parse():
        output = []

        with open("config") as f: # parse config file for information
            for i in f:
                output.append(re.search("[^:]*$", i).group().strip())

        return output[0], int(output[1]), output[2]



    def generate(host, port, database):
        # Determine custom database
        if database == None:
            database = "log.db"

        f = open("config", "w")
        f.write(f"Host: {host}\nPort: {port}\nDatabase: {database}")
