import string
import sys
import os
import time

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

for t in range(param-1):
        matrix = [(x+y) for x in matrix for y in alphabet]
        for value in matrix:
                time.sleep(0.5)
                name = "{}.com".format(value)
                result = os.popen("host {}".format(name)).read()
                if "not found" in result:
			file = open("host_output.txt", "a")
                        file.write(result + '\n')
                        file.close()

