"""
CIS 210 STYLE
CIS 210 W19 Project 2-2

Author: [Jacob Rammer]

Credits: [N/A]

# TODO desc
"""
from math import sqrt


def main():
    '''Square root comparison program driver.'''

    # sqrt_compare(25, 5)
    # sqrt_compare(25, 10)
    # sqrt_compare(625, 5)
    # sqrt_compare(625, 10)
    # sqrt_compare(10000, 8)
    # sqrt_compare(10000, 10)
    # sqrt_compare(10000, 11)

    return None


def mysqrt(n, k):
    x1 = n

    for i in range(k):
        average = n / x1
        x1 = (x1 + average) / 2

    return x1


def sqrt_compare(num, iterations):

    print("For", num, "using", iterations, "iterations:")

    mysqrt_value = mysqrt(num, iterations)
    print("mysqrt value is: ", mysqrt_value)

    lib_val = sqrt(num)
    print("math lib val is: ", lib_val)

    error_val = round(((mysqrt_value - lib_val) / lib_val) * 100, 2)
    print("This is a:", error_val, "percent error")

    return None


main()