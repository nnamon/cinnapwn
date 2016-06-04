#!/usr/bin/python3

from .base import Payload
from .mischief.cat import Cat
from .mischief.debug import Debug

payloads = [
    #Cat(),
    Debug(),
]

class BasicPayload(Payload):

    def __init__(self):
        self.commands = []
        self.files = {}

        for i in payloads:
            for j in i.steps():
                self.commands.append(j)

        for i in payloads:
            for j in i.files.keys():
                self.files[j] = i.files[j]

    def steps(self):
        return self.commands

    def generate_script(self):
        output = "#!/bin/bash\n\n"
        for i in self.commands:
            output += i + "\n"
        return output
