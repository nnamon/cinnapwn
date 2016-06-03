#!/usr/bin/python3

from .base import Module
from ..payloads.noppayload import NOPPayload

class Debug(Module):
    """Prints debugger messages"""

    payload = NOPPayload()

    def detect(self, target):
        self.generate_traffic(target)
        return True

    def compromise(self, target, detect_val):
        self.generate_traffic(target)
        return True

    def generate_traffic(self, target):
        import time
        import random
        print("debug %s..." % target)
        print("debugged %s" % target)

