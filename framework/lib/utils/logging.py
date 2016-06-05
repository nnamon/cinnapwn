#!/usr/bin/python3

flags = {'success': True,
         'info': True,
         'failure': False,
         }

def success(target, msg):
    if flags['success']:
        print("[+] (%s): %s" % (target["ip"], msg))

def info(target, msg):
    if flags['info']:
        print("[*] (%s): %s" % (target["ip"], msg))

def failure(target, msg):
    if flags['failure']:
        print("[-] (%s): %s" % (target["ip"], msg))
