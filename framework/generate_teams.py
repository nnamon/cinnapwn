#!/usr/bin/python

import json

teams = file("../recon/teamlist").read().strip().split("\n")
ignore = ["NUS Grayhats", "NUS Greyhats"]

def main():
    targets = []
    for i in range(len(teams)):
        template = {"team": teams[i],
                    "ip": "192.168.1.%d" % (i + 65),
                    "compromised": False,
                    "ignore": False}
        if teams[i] in ignore:
            template['ignore'] = True
        targets.append(template)
    file("targets.json", 'w').write(json.dumps(targets))

if __name__ == "__main__":
    main()
