#!/usr/bin/python

# Importing socket library
import socket

#display hostname
#IP address
def get_Host_name_IP():
	try:
		host_name = socket.gethostname()
		host_ip = socket.gethostbyname(host_name)
		print("Hostname : ",host_name)
		print("IP : ",host_ip)
	except:
		print("Unable to get Hostname and IP")

# Driver code
get_Host_name_IP() 
