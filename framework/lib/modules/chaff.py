#!/usr/bin/python3

from .base import Module

"""Throws chaff traffic at the target"""

class Chaff(Module):

    ip_pattern = "10.10.11.%d"
    payload = None # No payload required
    tcp_conns = [21, 80, 443]

    def detect(self, target):
        """Constantly fuzz the network traffic of the target to hide other
        ongoing attacks"""
        self.generate_traffic(target)
        return True

    def compromise(self, target, detect_val):
        """Likewise"""
        self.generate_traffic(target)
        return True

    def generate_traffic(self, target):
        print("shoot %s..." % target)
        time.sleep(random.randrange(2, 5))
        print("shot %s" % target)

