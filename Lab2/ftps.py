# Lab 2 - CSE 3461
# Socket Programming

# Sonny Shi
# shi.354@osu.edu

 # Echo server program
import socket
import os
import sys
import hashlib

HOST = ''                 # Symbolic name meaning all available interfaces
PORT =int(sys.argv[1])              # Arbitrary non-privileged port

# Creates recv directory
directory = "recv"

if not os.path.exists(directory):
    os.makedirs(directory)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

# Gets the file size in the next 4 bytes
data = conn.recv(4)
print("File Size", data.decode('utf-8'))

# Gets the filename in the next 20 bytes (encoded in utf-8 so max string length is 20)
data = conn.recv(20)
newfilename = data.decode('utf-8').strip()
print("File Name", newfilename)
newfile = open("recv/"+newfilename, "wb")

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

# MD5 Checksum checking as seen in Lab1

newfile = open("recv/"+newfilename, "rb")
file = open(newfilename, 'rb')

oldhash = hashlib.md5()
newhash = hashlib.md5()

print("Hashing MD5 checksum for both files...")

# Loop to hash the MD5 checksum for both files

chunksize = 1000
while True:
	data = file.read(chunksize)
	newdata = newfile.read(chunksize)
	if data:
		oldhash.update(data)
		newhash.update(newdata)

	else:
		break

print("The two files are bitwise identical: " + str(oldhash.hexdigest() == newhash.hexdigest()))

# Always close your streams

file.close()
newfile.close()
