#!/usr/bin/env python

"""
A simple echo server
"""

import socket
import webbrowser

host = ''
port = 50000
backlog = 5
size = 1024
url="http://localhost:8090/test2.flv"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        webbrowser.open(url,2)
    client.close()
