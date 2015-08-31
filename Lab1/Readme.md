# CSE 3461 Lab 1: Python Binary File Copier and Validator

Sonny Shi, CSE 3461 Tue/Thur 12:45 PM Section

## To Run

1. Navigate to the folder containing the copy.py script
2. Run the following command:

	`python3 copy.py [Your File Here]`

	Where `[Your File Here]` is the file that you wish to copy

	<img src = "http://i.imgur.com/P3naipx.png">
3. Execute the script
	<img src = "http://i.imgur.com/WabAVeh.png">

## File location

The copied file will be located in the recv directory in the directory of the copy.py script

## File Validation

The copied file is validated by checking the hashed MD5 checksum. If the files are identical the following message will appear:

`The two files are bitwise identical: True`

Otherwise, the following message will appear:

`The two files are bitwise identical: False`

