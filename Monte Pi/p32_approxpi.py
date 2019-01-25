"""
Monte Pi
CIS 210 W19 Project 3-2

Author: [Jacob Rammer]

Credits: [N/A]

Approximate the value of pi using the
Monte Carlo algorithm.
"""
from random import random
from math import sqrt, pi


def isInCircle(x, y, r):
    """(Number, Number, Number) -> Bool

    This function determines if a point landed in a circle or not, returning True or False respectively.
    To do this, the coordinates are supplied to the x any y parameters, and r will be the radius of the circle. To
    find the distance, the variable will use a formula to find the distance between the origin of the circle and the
    random point if the point is within the circle, True will be returned.

    >>> isInCircle(0, 0, 1)
    True
    >>> isInCircle(0, .5, 1)
    True

    """
    distance = sqrt(x ** 2 + y ** 2)

    if distance <= r:
        return True
    else:
        return False


def montePi(numDarts):
    """(Int) -> Constant

    This function will approximate the value of pi by throwing a varying amount of darts, supplied by
    the numDarts parameter. Generate random x and y coordinates by looping numDarts times. While in the loop, call
    function isInCircle to get boolean value and increase the number of darts that landed in the circle (inCircle)
    by 1 if the returned value is true. After the loop is finished, pi will be approximated by dividing the number of
    darts inCircle divided by numDarts * 4 returning the approximated value of pi.

    >>> montePi(300)
    3.16
    >>>montePi(50000)
    3.13784


    """
    inCircle = 0

    for i in range(numDarts):
        x = random()
        y = random()

        if isInCircle(x, y, 1):
            inCircle += 1

    pi = inCircle / numDarts * 4
    return pi


def reportPi(numDarts, approxPi):  # is approxPi even needed?
    """(Number, Number) -> Number, Number

    This function calculates how close the approximated value of pie is to the real value of pi. The function
    calculates the percentage of error between the two values and stores the value in errorVal, and is later printed.
    Returns None.

    >>>(reportPi(500, 3.2))
    With 100 iterations:
    my approximate value for pi is: 3.1616516516516517
    math lib pi value is:  3.141592653589793
    This is a 1.01 percent error.

    >>> reportPi(500, 3.2)
    With 500 iterations:
    my approximate value for pi is: 3.1616516516516517
    math lib pi value is:  3.141592653589793
    This is a 1.02 percent error.


    """

    print("With", numDarts, "iterations:\nmy approximate value for pi is:", approxPi)
    print("math lib pi value is: ", pi)

    errorVal = round(approxPi / pi, 2)
    print("This is a", errorVal, "percent error.")

    return None


def main():
    montePi(255)
    reportPi()
