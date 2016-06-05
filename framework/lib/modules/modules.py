#!/usr/bin/python3

from . import chaff
from . import debug
from . import vsftpdbd
from . import defaultpass
from . import msfssh
from . import droppedssh
from . import pyx

MODULES = [
#    chaff.Chaff(),
#    debug.Debug(), # Uncomment this to test if the loader is working
#    msfssh.MSFSSHDefaultPassword(),

    defaultpass.SSHDefaultPassword(),
    vsftpdbd.VSFTPdBackdoor(),
    droppedssh.SSHDropped(),
]

# Exploit the persistence
CODULES = [
    droppedssh.SSHDropped(),
    pyx.PyxBackdoor(),
    vsftpdbd.PatchedVSFTPdBackdoor(),
]
