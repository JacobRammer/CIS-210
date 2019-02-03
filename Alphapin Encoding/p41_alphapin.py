"""
Alphapin Encoding and Decoding
CIS 210 W19 Project 4-1

Author: [Jacob Rammer]

Credits: [N/A]

Encode and decrypt pin numbers
"""

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwyz"


def alphapinEncode(pin):
    """(int) -> string

    This function will encrypt the pin parameter provided and will return it as a string with alternating constant and
    vowels. Assigns letters based on location

    >>> alphapinEncode(5165)
    'nera'
    >>> alphapinEncode(6198191965198194196)
    'cefuveyezenezofuleze'

    """

    encodedPin = ""

    while pin > 0:
        lastTwoDig = pin % 100
        encodedPin = VOWELS[lastTwoDig % 5] + encodedPin
        encodedPin = CONSONANTS[lastTwoDig // 5] + encodedPin

        pin = pin // 100  # removes the last two digits from pin

    return encodedPin


def findConst(tone):
    """(str) -> str

    finds the constants in a given string (tone) and returns them. Given the string is formatted correctly:
    (constant, vowel, constant)

    >>> findConst("dafi")
    'df'
    >>> findConst("joke")
    'jk'

    """
    constants = tone[::2]
    return constants


def findVowel(tone):
    """(str) -> str

    finds the vowels in a given string (tone) and returns them. Given the string is formatted correctly:
    (constant, vowel, constant)


    >>> findVowel("joke")
    'oe'
    >>> findVowel("dafi")
    'ai'

    """
    vowels = tone[1::2]

    return vowels


def checkTone(tone):
    """(str) -> bool

    Checks to see if the tone is in the right format of (constant, vowel, constant) and returns True if string
    is formatted correctly of false if not.

    >>> checkTone("loohi")
    False
    >>> checkTone("lohi")
    True

    """
    # constants = tone[::2]
    # vowels = tone[1::2]

    constants = findConst(tone)
    vowels = findVowel(tone)
    for c, v in zip(constants, vowels):
        if c in CONSONANTS and v in VOWELS:
            pass
        else:
            return False
    return True


def alphapinDecode(tone):
    """(str) -> int or -1

    Decode the string produced by alphapinEncode and return the original number if the string is formatted correctly
    or -1.

    >>> alphapinDecode("hipu")
    2759
    >>> alphapinDecode("dizo")
    1298

    """

    if checkTone(tone):
        decodedPin = 0

        # constants = tone[::2]
        # vowels = tone[1::2]
        constants = findConst(tone)
        vowels = findVowel(tone)

        for c, v in zip(constants, vowels):
            decodedPin = decodedPin * 100 + CONSONANTS.index(c) * 5 + VOWELS.index(v)

        return decodedPin
    else:
        print("Tone is not in correct format.")
        return -1


def main():
    """Program driver for p41"""

    pin = int(input("What number would you like to encode? "))
    decodePin = alphapinEncode(pin)
    print(decodePin)
    print(alphapinDecode(decodePin))


main()
