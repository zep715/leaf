import sys


def usage():
    print ("start [range]")
    sys.exit(1)


def run(opts):
    if len(opts) < 1:
        usage()
    rname = opts[0]
    print ("range to start is {}".format(rname))
    print ("start")
    pass
