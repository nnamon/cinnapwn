#!/usr/bin/python3

from ..base import Payload

class Debug(Payload):

    files = {"cat.ascii": "/tmp/cat"}

    def __init__(self):
        self.commands = []
        self.commands.append("uname -a | wall")

    def steps(self):
        return self.commands


