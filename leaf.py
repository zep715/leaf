#!/usr/bin/python3
import sys
import commands


def usage():
    print ("usage: [start|stop|status] command [...]")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    if not hasattr(commands, sys.argv[1]):
        print("unknow command")
        usage()
    command = getattr(commands, sys.argv[1])
    command.run(sys.argv[2:])
