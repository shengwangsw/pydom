import string
import sys
import time
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

for t in range(param-1):
        matrix = [(x+y) for x in matrix for y in alphabet]
        for value in matrix:
                time.sleep(0.5)
                name = "{}.com".format(value)
                try:
                        w = whois.whois(name)
                        #print('\tTAKEN')
                except (whois.parser.PywhoisError):
                        # Exception means that the domain is free
                        #print('\tFREE')
                        f = open('free-domains.txt', 'a')
                        f.write(name + '\n')
                        f.close()
