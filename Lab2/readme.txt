CSE 3461 Lab 2: Python Socket Programming

Sonny Shi, CSE 3461 Tue/Thur 12:45 PM Section

To Run

	1. Navigate to the folder containing the copy.py script
	2. Run the following command:

		python3 ftps.py <Port Number>

		Where <Port Number> is the port you wish to use

		This will start the server.

	3. Run the following command:

		python3 ftpc.py <remote-IP-on-gamma> <remote-port-on-gamma> <local-file-to-transfer>

	4. The program will transfer the file and then do a MD5 checksum comparison to ensure the files are the same

File location

	The transferred file will be located in the recv directory in the directory of the ftps.py and ftpc.py scripts