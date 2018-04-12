import string
import itertools
import hashlib
import sys
import fileinput
import os

def main():
    # Check cmd line arguments
    if len(sys.argv) != 2:
        print("{}".format("Usage: application.py file checksum"))
        exit(1)

    # Store  file and checksum
    checksum = sys.argv[2]

    # Instantiate hash function
    contenthash = hashlib.sha256().hexdigest()

    # Open file to verify

    with open(sys.argv[1], "r+b") as Sub:
        Sub.seek(0)
    contenthash.update(Sub)

    # Compare checksum and hash from file
    if (compare(contenthash, checksum) != True):
        return 0
    else:
        return 1


def compare(filehashed, checksum):
    if filehashed == checksum:
        print("{}".format("Valid"))
        return True
    else:
        print("{}".format("Invalid"))
        return False


if __name__ == '__main__':
    main()
