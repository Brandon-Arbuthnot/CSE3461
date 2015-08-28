# Lab 1 - CSE 3461
# Copying files in Python

# Sonny Shi
# shi.354@osu.edu

# Write a  program called copy.py in Python  that reads a file and creates a copy of it in a sub-directory named recv 
# (on the same system). The program will be executed using the command python3 copy.py <filename> where filename is a 
# file in a local directory that needs to be copied. The program opens the file specified in the command line in binary 
# mode and creates a new file with the same name in the recv directory. In a loop, the program keeps reading the next 
# block of bytes (e.g., 1,000 bytes) from the file and writing it to the new file until all bytes have been read from 
# the file. Finally, the program closes the two files. 

import sys
import os

# File to copy and to write
filename = str(sys.argv[1])
file = open(filename, encoding='utf-8')
newfile = open("recv/"+filename, "w")

# Creates recv directory
directory = "recv"

if not os.path.exists(directory):
    os.makedirs(directory)

# Loops through original file and writes new file in the new directory
try:
	counter = 1
	byte = file.read(counter)
	newfile.write(byte)
	while byte != "":
		byte = file.read(counter)
		newfile.write(byte)
		counter = counter + 1
finally:
	file.close()
