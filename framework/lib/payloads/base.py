#!/usr/bin/python3

import base64

class Payload:

    commands = []
    files = {}

    def generate_script(self, prefix="./resources/"):
        output = "#!/bin/bash\n\n"

        for i in self.files:
            data = open(prefix + i, "rb").read()
            enc = base64.b64encode(data)
            enc = enc.decode("ascii")
            output += "chattr -i %s\n" % self.files[i]
            output += "chmod +w %s\n" % self.files[i]
            output += "printf '%s' | base64 -d > %s\n" % (enc, self.files[i])
            output += "chmod -w %s\n" % self.files[i]
            output += "chattr +i %s\n" % self.files[i]

        for i in self.commands:
            output += i + "\n"
        return output
