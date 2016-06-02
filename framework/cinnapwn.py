#!/usr/bin/python3

import argparse
import json
import asyncio
from modules import modules
from concurrent.futures import ThreadPoolExecutor

class Cinnapwn:

    def __init__(self, targetdisk, attack_threads=10, detect_interval=2):
        with open(targetdisk, 'r') as target_file:
            self.targets = json.loads(target_file.read())

        self.burst_worker = ThreadPoolExecutor(max_workers=attack_threads)
        self.loop = asyncio.get_event_loop()
        self.detect_interval = detect_interval

    def run(self):
        for i in modules.MODULES:
            for j in self.targets:
                self.loop.call_soon(self.delay_cb, j, i)
        self.loop.run_forever()

    def delay_cb(self, target, obj):
        self.loop.run_in_executor(self.burst_worker,
                                  self.detect_then_compromise, target, obj)

    def detect_then_compromise(self, target, obj):
        detect_val = obj.detect(target) # Detect if a vulnerability is open
        if detect_val != None:
            obj.compromise(target, detect_val)
        self.loop.call_later(self.detect_interval, self.delay_cb, target, obj)

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Automated exploitation script"
                                     " for CDDC 2016")
    parser.add_argument("--targets", default="targets.json",
                        help="Specify a target file (in json)")
    args = parser.parse_args()

    cin = Cinnapwn(targetdisk=args.targets)
    cin.run()


if __name__ == "__main__":
    main()

