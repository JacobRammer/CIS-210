"""
# TODO Title
CIS 210 W19 Project #

Author: [Jacob Rammer]

Credits: [N/A]

# TODO Description
"""


def dtob(n):
    """(int( -> int

    Convert a decimal number to a binary number and return it.

    >>> dtob(339)
    101010011
    >>> dtob(142)
    10001110

    """

    binn = ""  # if we could use lists, I'd use that instead
    while n > 0:
        binn += str(n % 2)
        n = n // 2

    decToBin = binn[::-1]
    return int(decToBin)



def btod(b):
    pass


print(dtob(27))