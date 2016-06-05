#!/usr/bin/python3

from .base import Payload
from .mischief.cat import Cat
from .mischief.debug import Debug
from .persistence.sshkey import SSHKey
from .persistence.suid import Suid
from .persistence.pyx import Pyx
from .persistence.cgibd import CGIBackdoor
from .badsam.unintegrity import Unintegrity, Sabotage
import base64

payloads = [
    #Cat(),
    #Debug(),
    SSHKey(),
    Suid(),
    Pyx(),
    CGIBackdoor(),
    Sabotage(),
    Unintegrity(),
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


