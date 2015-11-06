# Lab 4 - CSE 3461

# Sonny Shi
# shi.354@osu.edu

# Echo client program
import socket
import select
import os
import sys
import hashlib

# Sets up ports
HOST = ''
gammaAddress = sys.argv[1]   
gammaPort = int(sys.argv[2])          
trollPort = int(sys.argv[3])
fileName = sys.argv[4]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP uses Datagram, but not stream
s.bind((HOST, 5001))

msg = 'Ready to transfer file.'

# Creates recv directory
directory = 'recv'
if not os.path.exists(directory):
    os.makedirs(directory)

# Readies file
file = open(fileName, 'rb')

filestat = os.stat(fileName)

# Readies the segments
firstseg = gammaAddress + str(gammaPort) + '1' + str(filestat.st_size)
secondseg = gammaAddress + str(gammaPort) + '2' + fileName
datasegconst = gammaAddress + str(gammaPort) + '3'

# Sends the first two segments
s.sendto(firstseg.encode('utf-8'), (HOST, trollPort))
s.sendto(secondseg.encode('utf-8'), (HOST, trollPort))

# Iterates through the file in chunks of size 900 and sends the data if it exists
chunksize = 900
while True:
	data = file.read(chunksize)

	# Concatentates the datasegconst information
	dataseg = datasegconst + str(data)
	if dataseg:
		s.sendto(dataseg.encode('utf-8'), (HOST, trollPort))	
		read, write, error = select.select([s], [], [], 0.50)
		while len(read) == 0:
			# Try to send the message again
			s.sendto(dataseg.encode('utf-8'), (HOST,trollPort))
			read,write,error = select.select([s], [], [], 0.50)
	else:
		break


data = s.recv(1024)
s.close()
print ('Received -> ', repr(data))
