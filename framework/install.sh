#!/bin/bash

apt-get update
apt-get install python3 python3-dev python3-pip git
apt-get install libffi-dev
apt-get install libssl-dev
pip3 install cryptography
pip3 install --upgrade git+https://github.com/arthaud/python3-pwntools.git
pip3 install --upgrade git+https://github.com/nnamon/pymetasploit.git
