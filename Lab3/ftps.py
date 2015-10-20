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

