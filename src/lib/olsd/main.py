import daemon
import datetime
import os

home = os.path.expanduser("~")
def main():
    with open(f"{home}/.local/share/OLS/logs/events.log", "a"):
        pass
    while True:
        pass

with daemon.DaemonContext():
    main()