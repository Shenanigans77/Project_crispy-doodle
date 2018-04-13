import hashlib
import sys
import os
import io


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

# compare takes two arguments, both strings
# one should be the hash of a file, the other should be a checksum
def compare(filehashed, checksum):

    if filehashed == checksum:
        print("{}".format("Valid"))
        return True
    else:
        print("{}".format("Invalid"))
        return False


# Takes a file as an argument. Returns the hex digest of the file
def hcalc(intake):
    # Instantiate hash function
    filehash = hashlib.sha256()

    # Calculate specified hash values
    with open(intake, "r+b") as fintake:

        # reads fintake as a stream of bytes
        filebytes: object = io.BufferedRandom(fintake).read()

        # updates contents to hash
        filehash.update(filebytes)

        digested = filehash.hexdigest()

    return digested


if __name__ == '__main__':
    main()
