import socket
import string
import sys
try:
	import whois
except ImportError:
	print("ERROR: This script requires the python-whois module to run.")
	print("   You can install it via 'pip install python-whois'")
	sys.exit(0)

if len(sys.argv) < 2:
	print("You should add an argument")
	print("   Try 'python findomain.py <argument>'")
	sys.exit(0)

if not sys.argv[1].isdigit():
	print("Argument must be a number")
        print("   Try 'python findomain.py <number>'")
        sys.exit(0)

param = int(sys.argv[1])

if param < 2:
	print("Argument must be greater than 1")
	print("Domain with one character or number is already taken")
        print("   Try 'python findomain.py <number>'")
        sys.exit(0)

alphabet = list(string.ascii_lowercase)
matrix = alphabet

for t in range(0):
	matrix = [(x+y) for x in matrix for y in alphabet]
	file = open("output", "a")
	for value in matrix:
		name = "{}.com".format(value)
		try:
			domain = socket.gethostbyname(name)
		except socket.gaierror:
			file.write(name)
	file.close()

