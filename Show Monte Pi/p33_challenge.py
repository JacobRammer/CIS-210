'''
Approximating pi.  CIS 210 W19 Project 3-3
Starter Code for showMontePi

Author: Jacob Rammer

Credits: Based on code on p.78 Miller and Ranum text.

Approximate pi using a Monte Carlo simulation.
Then add graphics to visualize simulation.
'''

from turtle import *
from math import sqrt, pi
import random


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


def drawBoard():
    """

    This function hides the Turtle cursor and draws the x and y axis on a graph. Returns None.

    >>> drawBoard()
    draws x, y, axis
    """

    speed(0)
    hideturtle()
    penup()

    goto(-1, 0)  # draw graph axis
    pendown()
    goto(1, 0)
    penup()
    goto(0, 1)
    pendown()
    goto(0, -1)
    penup()
    goto(0, -1)

    return None


def showMontePi(numDarts, draw=False):
    '''
    DOCSTRING written according to
    210 style guidelines goes here
    '''

    if draw:
        wn = Screen()
        wn.setworldcoordinates(-2, -2, 2, 2)

        drawBoard()

    # pen should stay up for drawing darts

    inCircle = 0

    # throw the darts and check whether
    # they landed on the dart board and
    # keep count of those that do

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        if isInCircle(x, y, 1):
            inCircle += 1
        if draw:
            if isInCircle(x, y, 1):
                color('blue')
            else:
                color('red')
            goto(x, y)
            dot()

    # calculate approximate pi
    approxPi = inCircle / numDarts * 4

    if draw:
        exitonclick()

    return approxPi


def reportPi(numDarts, approxPi):
    """(Number, Number) -> None

    This function calculates how close the approximated value of pie is to the real value of pi. The function
    calculates the percentage of error between the two values and stores the value in errorVal, and is later printed.
    Returns None.

    Note: Random x and y values are chosen at random. Exact values may  not be replicable.

    >>> reportPi(500, 3.2))
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
    """driver for show Monte Pi project"""

    reportPi(100, showMontePi(100))

    return None


main()
