"""
Drawing with Python
CIS 210 W19 Project 2-3

Author: [Jacob Rammer]

Credits: [N/A]

Use python's Turtle module to draw
various types of graphics
"""
from turtle import *


def drawFlower(numSquares):
    """(Int) -> Turtle Object

    Draw a square numSquare times by calling drawPolygon()
    function to draw the petals on a flower. turn_angle will
    rotate the turtle cursor an even amount times based
    upon how many squares are to be drawn. Void function

    >>>drawFlower(5)
    will draw a square 5 times and rotate it

    """
    rt(270)
    fd(100)

    turn_angle = 360 / numSquares

    for i in range(numSquares):
        drawPolygon(35, 4)  # I know the assignment says 25, but 25 seems too small
        rt(turn_angle)

    return None


def drawPolygon(sideLength, numSides):
    """(Int, Int) -> Turtle object

    Draw an object based upon supplies arguments. sideLength will
    be how long the side of the object is, and numSides will be
    how many sides the object has. turnAngle is needed in order
    to determine how many times the turtle cursor rotates to draw
    the shape of the object.

    >>>drawPolygon(25, 4)
    will draw a square with a side length of 25

    >>>drawPolygon(25, 5)
    will draw a pentagon with side length of 25

    """

    turnAngle = 360 / numSides

    for i in range(numSides):
        fd(sideLength)
        rt(turnAngle)

    return None


def main():
    """
    Main function to start script by calling drawFlower()

    :return: None
    """
    drawFlower(25)

    return None


main()

