#!/usr/bin/python3

"""
Program: caesar2.py
Decription: a simple script to encode/decode a text message with a Caesar cipher and a codeword
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

    Codeword = input("Enter the codeword: ")
    Message = input("Enter the message to be encrypted/decrypted: ")
    ToDo = input("Enter e to encrypt or d to decrypt the message: ")

    # adjusting the codeword

    Codeword = Codeword.upper()
    Codeword_len = len(Codeword)
    for i in range(0, Codeword_len):  # we don"t want any double letters
        if Codeword.count(Codeword[i]) > 1:  # in a monoalphabetical substitution
            dummy = Codeword[i]  # so let"s try to get rid of them
            Codeword = Codeword.replace(Codeword[i], " ")
            Codeword = Codeword.replace(" ", dummy, 1)
    Codeword = Codeword.replace(" ", "")  # no blanks
    Codeword_len = len(Codeword)  # it might be shorter now

    # adjusting the cipher or alphabet

    if ToDo == "e":
        Cipher = Codeword + Cipher
        for i in range(0, len(Cipher)):
            if Cipher.count(Cipher[i]) > 1:
                dummy = Cipher[i]
                Cipher = Cipher.replace(Cipher[i], " ")
                Cipher = Cipher.replace(" ", dummy, 1)
        Cipher = Cipher.replace(" ", "")
        print (Cipher, len(Cipher))
    elif ToDo == "d":
        Alphabet = Codeword + Alphabet
        for i in range(0, len(Alphabet)):
            if Alphabet.count(Alphabet[i]) > 1:
                dummy = Alphabet[i]
                Alphabet = Alphabet.replace(Alphabet[i], " ")
                Alphabet = Alphabet.replace(" ", dummy, 1)
        Alphabet = Alphabet.replace(" ", "")
    else:
        print ("Please use only e or d.")
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
    print ("Codeword: ", Codeword)
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
