"""
Fizzbuzz
CIS 210 W19 Project 3-1

Author: [Jacob Rammer]

Credits: [N/A]

Check to see if a number is dividable
by 3 or 5 and print the respective fizz
or buzz.
"""


def fb(n):
    """(Int) -> Int, or String

    Enter a number n, and check to see
    if it's divisible by 3 or 5 and print
    either fizz or buzz respectively.
    If the number is not divisible by either,
    print the number. If n is
    divisible by both, print fizzbuzz. Will be
    accomplished by using a for loop and incrementing
    i on each pass.

    >>> fb(5)
    1
    2
    fizz
    4
    buzz
    Game over!
    >>> fb(3)
    1
    2
    fizz
    Game over!

    """

    for i in range(n):
        i += 1

        if (i % 3 == 0) and (i % 5 == 0):
            print("fizzbuzz")
        elif (i % 3 == 0):
            print("fizz")
        elif (i % 5 == 0):
            print("buzz")
        else:
            print(i)

    print("Game over!")

    return None
