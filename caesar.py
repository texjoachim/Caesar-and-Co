#!/usr/bin/python3

"""
Program: caesar.py
Decription: a simple script to encode/decode a text message with a Caesar cipher
Author: Joachim Ziebs
Version: 0.0.1
Licence: GPL v3 or later
"""

# Imports
import sys


# Main

def main():

    # necessary variables

    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Cipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # getting input

    Move = int(input("Enter how far the characters should be moved: "))
    Message = input("Enter the message to be encrypted/decrypted: ")

    # adjusting the cipher or alphabet

    if Move > 0:
        Cipher = Cipher[len(Cipher) - Move:len(Cipher)] \
            + Cipher[0:len(Cipher) - Move]
    elif Move < 0:
        Move = -Move
        Alphabet = Alphabet[len(Alphabet) - Move:len(Alphabet)] \
            + Alphabet[0:len(Alphabet) - Move]
    else:
        print ("Please enter a positive or negative number, but not zero.")
        sys.exit(0)

    # getting the message ready

    Message = Message.replace(" ", "")  # no blanks
    Message = Message.upper()  # only upper case

    # creating a translation table

    dummy = ""
    Caesar_table = dummy.maketrans(Alphabet, Cipher)

    # encoding or decoding the message

    Secret = Message.translate(Caesar_table)

    # Output

    print ("")
    print ("######################################################################")
    print ("Alphabet: ", Alphabet)
    print ("Cipher: ", Cipher)
    print ("Message: ", Message)
    print ("Secret message: ", Secret)
    print ("######################################################################")
    print ("")

    sys.exit(0)


# Execute!

if __name__ == "__main__":
    main()
