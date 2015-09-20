 # Echo server program
import socket
import os
import sys

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 5000              # Arbitrary non-privileged port

# Creates recv directory
directory = "recv"

if not os.path.exists(directory):
    os.makedirs(directory)

newfile = open("recv/file", "wb")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)
while 1:
    data = conn.recv(1024)
    newfile.write(data)
    if not data: break
    conn.sendall(data)
conn.close()



