import hashlib
import sys
import fileinput
import os

def main():
    # Check cmd line arguments
    if len(sys.argv) != 2:
        print("{}".format("Usage: application.py file"))
        exit(1)

    # Store  file and checksum

    checksum = input("Paste checksum here: ")
    # Calculate specified hash values
    with fileinput.FileInput(files=(sys.argv[1]), mode='rb') as intake:
        filehash = hashlib.sha256(intake).hexdigest()

    compare(filehash, checksum)

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
