import hashlib
import sys
import fileinput
import os


def main():
    # Check cmd line arguments
    if len(sys.argv) != 2:
        print("{}".format("Usage: application.py file"))
        exit(1)

    # Calculate sha256 hash for desired file
    targetfile = hcalc(sys.argv[1])
    print("{}".format(targetfile))

    # Store checksum
    checksum = input("Paste checksum here: ")

    compare(targetfile, checksum)

    return 0


def compare(filehashed, checksum):
    if filehashed == checksum:
        print("{}".format("Valid"))
        return True
    else:
        print("{}".format("Invalid"))
        return False


def hcalc(intake):
    # Instantiate hash function
    filehash = hashlib.sha256()

    # Calculate specified hash values
    with open(intake, "r+b") as fintake:
        filehash.update(str(fintake).encode("utf-8"))
        digested = filehash.hexdigest()

    return digested


if __name__ == '__main__':
    main()
