#!/usr/bin/python3

from .base import Module

"""Throws chaff traffic at the target"""

class Chaff(Module):

    ip_pattern = "10.10.11.%d"

    def detect(self, target):
        self.generate_traffic(target)
        return True

    def compromise(self, target, detect_val):
        self.generate_traffic(target)
        return True

    def generate_traffic(self, target):
        import time
        import random
        print("shoot %s..." % target)
        time.sleep(random.randrange(2, 5))
        print("shot %s" % target)

