#!/usr/bin/python

import json

teams = ["dysnar", "test1"]

def main():
    targets = []
    for i in range(len(teams)):
        targets.append({"team": i, "ip": "192.168.1.%d" % (i + 65)})
    file("targets.json", 'w').write(json.dumps(targets))

if __name__ == "__main__":
    main()
