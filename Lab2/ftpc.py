# Echo client program
import socket
import os
import sys

HOST = 'gamma'    # The remote host
PORT = 5000              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

filename = str(sys.argv[3])
file = open(filename, 'rb')

# Sends the file size in the first four bytes
s.sendall(str(os.stat(filename).st_size).encode())

# Sends the file name in the next 20 bytes, assuming the name fits
s.sendall(filename.encode())

# Iterates through the file in chunks of size 1000 and sends the data if it exists
chunksize = 1000
while True:
	data = file.read(chunksize)
	if data:
		s.sendall(data)
	else:
		break

data = s.recv(1024)

#Close your streams!
s.close()
file.close()
print ('Received', repr(data))
