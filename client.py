# An example script to connect to Google using socket
# programming in Python
import socket # for socket
import sys
import random

# create a socket object
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket successfully created")
except socket.error as err:
	print ("socket creation failed with error %s" %(err))

# default port for socket
port = 1999

# default host ip
try:
	host_ip = socket.gethostbyname('127.0.0.1')
except socket.gaierror:

	# this means could not resolve the host
	print ("there was an error resolving the host")
	sys.exit()

# connecting to the server
s.connect((host_ip, port))

serverResponse = s.recv(1024).decode()

#split range of years
range = serverResponse.split(',')
print(range)

# Get client input
clientInput = input("Enter a year between 1950 and 2009: ")

#ensure client response is in range, if not print random year and song
if int(clientInput) < int(range[0]) or int(clientInput) > int(range[1]):
	print("Year not in range, here is a random year and song")
	
	#generate random year
	year = random.randint(1950,2009)
				   
	print(year) #testing
	s.send(str(year).encode())

else:
    s.send(clientInput.encode())

# Get server response
serverResponse = s.recv(1024).decode()
print(serverResponse)