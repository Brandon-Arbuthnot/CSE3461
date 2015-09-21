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


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(4)
print("File Size", data)
data = conn.recv(20)
print("File Name", data)
newfile = open("recv/"+data, "wb")
print ('Connected by', addr)
while 1:
    data = conn.recv(1000)
    # Writes the data to the file when it receives it
    newfile.write(data)
    if not data: break
    conn.sendall(data)

# Close your streams!
conn.close()
newfile.close()