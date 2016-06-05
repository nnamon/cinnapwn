#!/usr/bin/python3

import argparse
import json
import asyncio
import signal
from lib.modules import modules
from concurrent.futures import ThreadPoolExecutor
from lib.utils import common
import pwnlib.context
import http.server
import socketserver
import os

class Cinnapwn:

    def __init__(self, targetdisk, attack_threads=20, detect_interval=2):
        with open(targetdisk, 'r') as target_file:
            self.targets = json.loads(target_file.read())

        self.burst_worker = ThreadPoolExecutor(max_workers=attack_threads + 1)
        self.loop = asyncio.get_event_loop()
        self.detect_interval = detect_interval
        self.hook_signal()
        self.setup_server()

    def setup_server(self):
        Handler = http.server.SimpleHTTPRequestHandler
        self.httpd = socketserver.TCPServer(("", common.http_port), Handler)

    def run_http_server(self):
        # Always expected to run in the resources context, since there is no
        # need for any other location. Also, safety.
        os.chdir("./resources")
        sa = self.httpd.socket.getsockname()
        print("Serving HTTP on", sa[0], "port", sa[1], "...")
        self.httpd.serve_forever()

    def hook_signal(self):
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, signum, frame):
        self.loop.stop()
        self.burst_worker.shutdown(wait=False)
        self.httpd.server_close()
        print("Stopping")

    def run(self):
        self.loop.run_in_executor(self.burst_worker,
                                  self.run_http_server)

        for j in self.targets:
            for i in modules.MODULES:
                self.loop.call_soon(self.delay_cb, j, i)

        self.loop.run_forever()

    def delay_cb(self, target, obj):
        self.loop.run_in_executor(self.burst_worker,
                                  self.detect_then_compromise, target, obj)

    def detect_then_compromise(self, target, obj):
        detect_val = obj.detect(target) # Detect if a vulnerability is open
        if detect_val != None:
            if obj.compromise(target, detect_val):
                target['compromised'] = True
        self.loop.call_later(self.detect_interval, self.delay_cb, target, obj)

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Automated exploitation script"
                                     " for CDDC 2016")
    parser.add_argument("--targets", default="targets.json",
                        help="Specify a target file (in json)")
    parser.add_argument("--interval", default=10.0, type=float, help="Tick rate")
    args = parser.parse_args()

    cin = Cinnapwn(targetdisk=args.targets, detect_interval=args.interval)
    cin.run()


if __name__ == "__main__":
    main()

