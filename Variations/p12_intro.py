'''
CIS 210 W19 Project 1-2

Author: [Jacob Rammer]

Credits: [N/A]

number manipulations
'''


def convert(i, j, k):
    """ (str) -> int

    concatenate three integers and return the value

    >>> convert(1, 2, 3)
    321
    >>> convert(9, 8, 7)
    789
    """

    return str(k) + str(j) + str(i)


def add_digits(n):
    """ (int) -> int

    add three digits together and return the value

    >>> add_digits(111)
    3
    >>> add_digits(823)
    13
    """

    total = 0

    """
    this is a better way to accomplish task than a while loop. 
    It will also add x number of integers together
    """
    for i in str(n):
        total += int(i)

    return total


def profit(attendees):
    """ (int) -> float

    calculate the profit a movie theater will
    make per show and return profit. Tickets cost $5
    Calculation: Total - 20 - (.5 * attendees)

    >>>  profit(20)
    70
    >>> profit(15)
    47.5
    """

    theater_profit = (attendees * 5) - 20 - (attendees * .5)
    return theater_profit
