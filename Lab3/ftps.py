# Lab 3 - CSE 3461
# Socket Programming

# Sonny Shi
# shi.354@osu.edu

import socket
import os
import sys
import hashlib

HOST = ''
gammaPort = sys.argv[1]   

clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP uses Datagram, but not stream
clientsock.bind((HOST, int(gammaPort)))

print ('Waiting for packets...')
while True:
	# Gets packets
	data, addr = clientsock.recvfrom(1024)
	data = data.decode('utf-8')
	if not data: break

	# Finds the port number 
	pos = data.find(gammaPort)
	# Finds the flag
	flag = data[pos + len(gammaPort)]

	if flag == '1':
		filesize = int(data[pos + len(gammaPort) + 1:])
	if flag == '2':
		newfilename = data[pos + len(gammaPort) + 1:]
		newfile = open('recv/'+newfilename, 'wb')
	if flag == '3':
		strippeddata = data[pos + len(gammaPort) + 1:]
		newfile.write(strippeddata)
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