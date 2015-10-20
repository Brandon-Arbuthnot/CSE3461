# Echo client program
import socket
import os
import sys
import hashlib

# Sets up ports
HOST = 'localhost'
gammaAddress = sys.argv[1]   
gammaPort = int(sys.argv[2])          
trollPort = int(sys.argv[3])
fileName = sys.argv[4]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP uses Datagram, but not stream

msg = 'Ready to transfer file.'

# Creates recv directory
directory = 'recv'
if not os.path.exists(directory):
    os.makedirs(directory)

# Readies file
file = open(filename, 'rb')

filestat = os.stat(filename)

# Readies the segments
firstseg = gammaAddress + gammaPort + '1' + filestat.st_size
secondseg = gammaAddress + gammaPort + '2' + filename
datasegconst = gammaAddress + gammaPort + '3'

# Sends the first two segments
s.sendto(firstseg, (HOST, trollPort))
s.sendto(secondseg, (HOST, trollPort))

# Iterates through the file in chunks of size 900 and sends the data if it exists
chunksize = 900
while True:
	data = file.read(chunksize)
	# Concatentates the datasegconst information
	dataseg = datasegconst + data
	if dataseg:
		s.sendto(dataseg, (HOST, trollPort))
	else:
		break


data = s.recv(1024)
s.close()
print ('Received -> ', repr(data))