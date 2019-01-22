"""
CIS 210 STYLE
CIS 210 W19 Project 2-2

Author: [Jacob Rammer]

Credits: [N/A]

Find the square root of a number using the Babylonian
method, and comparing the results using the builtin
sqrt library and comparing the results.
"""
from math import sqrt


def mysqrt(n, k):
    """(Number, Int) -> Float

    To use the babylonian method, assign x1 to the
    initial value of n. Then loop through the calculations
    k times, dividing n and x1 to find the quotient between the two.
    Than find the average of the x1 and the quotient value and assign
    it to x1, returning the value of x1 after loop completion.

    >>> mysqrt(25, 1)
    13.0
    >>> mysqrt(10000, 8)
    101.20218365353946

    """
    x1 = n

    for i in range(k):
        quotient = n / x1
        x1 = (x1 + quotient) / 2

    return x1


def sqrt_compare(num, iterations):
    """(Number, Int)-> Float

    This functions compares the results from mysqrt() and
    the built in sqrt function. Create a value called
    mysqrt_value to store my mysqrt() function returns
    so it can be printed in an print statement and
    be used later to calculate accuracy. Create lib_value
    to use the builtin sqrt function, store the value,
    be printed, and referred back to to calculate accuracy.
    Error value calculates a percentage (rounded to 2 decimals)
    of discrepancy between the two. Returns void


    >>> sqrt_compare(100001, 10)
    For 100001 using 10 iterations:
    mysqrt value is:  317.20448317094645
    math lib val is:  316.2293471517152
    This is a: 0.31 percent error
    >>> sqrt_compare(100009, 11)
    For 100009 using 11 iterations:
    mysqrt value is:  316.24349564290105
    math lib val is:  316.2419959461425
    This is a: 0.0 percent error

    """
    print("For", num, "using", iterations, "iterations:")

    mysqrt_value = mysqrt(num, iterations)
    print("mysqrt value is: ", mysqrt_value)

    lib_val = sqrt(num)
    print("math lib val is: ", lib_val)

    error_val = round(((mysqrt_value - lib_val) / lib_val) * 100, 2)
    print("This is a:", error_val, "percent error")

    return None


def main():
    '''Square root comparison program driver.


    Returns None
    '''

    sqrt_compare(25, 5)
    sqrt_compare(25, 10)
    sqrt_compare(625, 5)
    sqrt_compare(625, 10)
    sqrt_compare(10000, 8)
    sqrt_compare(10000, 10)
    sqrt_compare(10000, 11)

    return None


main()
