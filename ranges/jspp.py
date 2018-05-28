import sys
import json


if __name__ == "__main__":
    fp = open(sys.argv[1], "r")
    j = json.loads(fp.read())
    fp.close()
    print json.dumps(j, indent=4)
