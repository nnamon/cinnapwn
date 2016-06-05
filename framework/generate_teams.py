#!/usr/bin/python

import json

teams = file("../recon/teamlist").read().split("\n")

def main():
    targets = []
    for i in range(len(teams)):
        template = {"team": teams[i],
                    "ip": "192.168.1.%d" % (i + 65),
                    "compromised": False}
        targets.append(template)
    file("targets.json", 'w').write(json.dumps(targets))

if __name__ == "__main__":
    main()
