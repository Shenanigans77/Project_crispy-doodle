import string
import itertools
import hashlib
import sys
import os

def main():
    # Check cmd line arguments
    if len(sys.argv) != 2:
        print("{}".format("Usage: application.py file checksum"))
        exit(1)

    # Store  file and checksum
    infile = sys.argv[1]
    checksum = sys.argv[2]
    # Calculate specified hash values
    # For completeness (not secure)
    contenthash = hashlib.sha256()
    open(infile, "r+b")


    # Compare 2 checksums to see if they are identical
    file = 'abc'
    check = 'abc'


    return 0


def compare(filehashed, checksum):
    if filehashed == checksum:
        print("{}".format("Valid"))
        return True
    else:
        print("{}".format("Invalid"))
        return False


if __name__ == '__main__':
    main()
