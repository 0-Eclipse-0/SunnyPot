#!/usr/bin/python3

import socket
import re
import os, signal
from datetime import datetime
from sys import exit
from time import sleep

# _______ Variables _________

if (os.path.exists("config.txt")):
    quick_config = True
else:
    quick_config = False

sp = "[SunnyPot] "
er = "[Error] "

sunnypot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# _______ Redundancy ________

# # _______ Classes ________
# class config:
#     ip =
#     port =
# _______ Functions _________

def keyboard_int:
    

def get_host_ip():
    try:
        host_ip = socket.gethostbyname(socket.gethostname())
        if host_ip == "127.0.0.1":
            host_ip = input(sp + " Could not resolve IP, enter IP manually: ") # Can't open honeypot
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host_ip): # Valid input ip
                pass
            else: # Invalid input ip
                exit(er + "Invalid IP Address. Exiting...")
        else:
            pass # Pass
    except Exception:
        sys.exit(er + "Error resolving hostname...")
        sunnypot.close
    return host_ip

def format_header(header):
    pass

def logging():
    if os.path.isdir("logs"):
        pass
    else:
        os.mkdir("logs")

def build_config():
    print("Test\n")
    pass

def start_pot(ip, port):
    # try:
    #     sunnypot.bind((ip,port))
    # except OSError:
    #     print(er + "Address still in use, waiting for connection to die...")
    #     sleep(10)
    #     exit(sp + "Connection dead. Exiting...")

    logging()
    sunnypot.listen(5)

    while True:
        sleep(1)
        attacker, (attacker_ip, attacker_port) = sunnypot.accept()
        print("-"*6, "Intrusion Detected", "-"*6, "\a\a\a")
        print("Connection from: %s:%s" % (attacker_ip, attacker_port))
        #print(format_header(header))
        attacker.close()

# ______ Main ______

if (quick_config):
    print(sp + "Running from config file, delete the file before compiling again if you'd like to run in single-use mode or modify the file...\n")
    sleep(5)
    config_vars()
else:
    #print(datetime.now().strftime('%H:%M'))
    mode = input(sp + "Select Mode (1 = Single-Use, 2 = Config Builder) >> ")

    if (mode == "1"):
        pot_ip = get_host_ip()

        try:
            pot_port = int(input(sp + "Enter Port >> "))
        except ValueError:
            exit(er + "Not a port! Exiting...")
        finally:
            if (0 < pot_port <= 65535):
                pass
            else:
                exit(er + "Port must be between 1 and 65,535. Exiting...")
        #sunnypot.bind((pot_ip, pot_port))
        start_pot(pot_ip, pot_port)
    elif (mode == "2"):
        build_config()
    else:
        exit(er + "Invalid option. Exitting...")
