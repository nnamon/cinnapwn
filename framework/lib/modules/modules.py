#!/usr/bin/python3

from . import chaff
from . import debug
from . import vsftpdbd
from . import defaultpass

MODULES =   [
#    chaff.Chaff(),
#    debug.Debug(), # Uncomment this to test if the loader is working
    defaultpass.SSHDefaultPassword(),
    vsftpdbd.VSFTPdBackdoor(),
]
