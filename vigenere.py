#!/usr/bin/python3
"""
Program: vigenere.py
Decription: a small script to encode/decode with a Vigenere cipher
Author: Joachim Ziebs
Version: 0.0.1
Licence: GPL v3 or later
"""

# Imports
import sys

"""
Eingabe von Schlüsselwort
Eingabe von Nachricht

Encodieren
    Kombination von Schlüsselwort und Zeichen der Nachricht\
    bis beide Teile gleich groß sind
    Addition der Kombination bis die Kombination größer oder\
    gleich der Nachricht ist
    (Abschneiden der überschüssigen Buchstaben)

    http://de.wikipedia.org/wiki/Polyalphabetische_Substitution

"""


# get rid of blanks and turn the string to upper case
def beautify(string):
    string = string.upper()
    string = string.replace(" ", "")  # no blanks
    return(string)


# creating the cipher
def create_cipher(k, m):
    k = beautify(k)
    k_len = len(k)
    m_len = len(m)
    cipher = ""
    while len(cipher) < m_len:
        for i in range(0, k_len):
            if len(cipher) < m_len:
                cipher = cipher + k[i]

    return(cipher)


# encrypt
def encrypt(k, m):
    nachricht = "leer"
    return(nachricht)


# decrypt
def decrypt(k, m):
    nachricht = "leer"
    return(nachricht)


# Main
def main():
    key = input("Enter the key: ")
    message = input("Enter the message: ")
    todo = input("Enter e for encryption or d for decryption.")

    #beautify the message
    message = beautify(message)

    # adjusting the codeword
    cipher = create_cipher(key, message)

    if todo != "e":
        if todo != "d":
            print("Usage: Please enter your key, your message and e for\
             encryption or d for decryption.")
            sys.exit(0)
    if todo == "e":
        result = encrypt(key, message)
    elif todo == "d":
        result = decrypt(key, message)

    # Here is what we can print out
    print ("")
    print ("######################################################################")
    print ("Key: ", key)
    print ("Message: ", message)
    print ("Cipher: ", cipher)
    print ("Secret message: ", result)
    print ("######################################################################")
    print ("")
    sys.exit(0)


# Execute!
if __name__ == "__main__":
    main()
