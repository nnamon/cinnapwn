#!/usr/bin/python

def hex_repr(string):
    return "".join(["\\x" + hex(ord(i))[2:].rjust(2, "0") for i in string])

def hex_reprb(string):
    return "".join(["\\x" + hex(i)[2:].rjust(2, "0") for i in string])

