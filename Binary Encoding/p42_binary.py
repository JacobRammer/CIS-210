"""
Binary to decimal
CIS 210 W19 Project 42

Author: [Jacob Rammer]

Credits: [N/A]

Convert binary to decimal and decimal to binary
"""
import doctest

def dtob(n):
    """(int) -> str

    Convert a decimal number to a binary string and return it.

    >>> dtob(339)
    '101010011'
    >>> dtob(142)
    '10001110'

    """

    if isinstance(n, int) and n > 0:  # challenge problem #1, check for int and positive #
        binn = ""
        while n > 0:
            binn += str(n % 2)
            n = n // 2

        return binn[::-1]
    else:
        print("Non-negative integer expected")
        exit()


def btod(b):
    """(str) -> int

    Convert a binary string into a decimal number and return it.

    >>> btod('1101')
    13
    >>> btod("1000111110")
    574

    """


    decimal = 0

    powOfTwo = 0  # will iterate on each for

    for i in b[::-1]:
        decimal += int(i) * (2 ** powOfTwo)
        powOfTwo += 1
    return decimal


def main():
    """Program driver"""

    number = int(input("Enter a non-negative integer: "))

    binNumber = dtob(number)
    print("Binary format is " + binNumber)

    decNumber = btod(binNumber)
    print("Back to decimal: ", decNumber)


print(doctest.testmod())
main()


