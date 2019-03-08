"""
Earthquake Watch
CIS 210 W19 Project 9-1

Author: [Jacob Rammer]

Credits: [N/A]

Graphing earthquakes with turtle graphics
"""
from math import sqrt
from random import randint
import turtle


def readFile(fileName="earthquakes.csv"):  # TODO change for class file
    """(str) -> dict"""

    datadict = {}
    key = 0

    with open(fileName) as equake_date:
        equake_date.readline()

        for line in equake_date:
            key += 1
            lat = line.split(",")[1]
            lon = line.split(",")[2]
            mag = line.split(",")[4]
            datadict[key] = [float(lon), float(lat), float(mag)]

    return datadict

# print(readFile("earthquakes.csv"))

def euclidD(point1, point2):

    total = 0

    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total = total + diff

    euclidDistance = sqrt(total)

    return euclidDistance


def createCentroids(k, datadict):

    centroids = []
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k:
        rkey = randint(1, len(datadict))
        if rkey not in centroidKeys:
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount = centroidCount + 1

    return centroids


def createClusters(k, centroids, datadict, repeats):

    for apass in range(repeats):
        print("**** PASS", apass, "****")
        clusters = []
        for i in range(k):
            clusters.append([])

        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey], centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances)
            index = distances.index(mindist)

            clusters[index].append(akey)

        dimensions = len(datadict[1])
        for clusterIndex in range(k):
                sums = [0] * dimensions
                for akey in clusters[clusterIndex]:
                    datapoints = datadict[akey]
                    for ind in range(len(datapoints)):
                        sums[ind] = sums[ind] + datapoints[ind]

                for ind in range(len(sums)):
                    clusterLen = len(clusters[clusterIndex])
                    if clusterLen != 0:
                        sums[ind] = sums[ind] / clusterLen

                centroids[clusterIndex] = sums

        for c in clusters:
            print("CLUSTER")
            for key in c:
                    print(datadict[key], end=" ")
            print()

    return clusters


def change_turtle_color():
    """() -> tuple

    Generate random color decimal codes for turtle plotting. Returns the RGB decimal code tuple.

    > change_turtle_color()
    (100, 150, 255)
    > change_turtle_color()
    (255, 255, 0)

    """
    turtle_color_r = randint(0, 255)
    turtle_color_g = randint(0, 255)
    turtle_color_b = randint(0, 255)
    print("color:", turtle_color_r, turtle_color_g, turtle_color_b)  # TODO delete

    return turtle_color_r, turtle_color_g, turtle_color_b


def visaulizeQuakes(dataFile, k=6, r=7):  # using values from book, k = clusters, r = repeat

    datadict = readFile(dataFile)
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)

    eqDraw(k, datadict, clusters)  # plotting points

    return None


def eqDraw(k, eqDict, eqClusters):

    quakeT = turtle.Turtle()
    turtle.colormode(255)
    quakeT.speed("fastest")
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap1800_900.gif")
    quakeWin.screensize(1800, 900)

    wFactor = (quakeWin.screensize()[0] / 2) / 180
    hFactor = (quakeWin.screensize()[1] / 2) / 90

    quakeT.hideturtle()
    quakeT.up()

    for clusterIndex in range(k):
        turtle_color_r, turtle_color_g, turtle_color_b = change_turtle_color()
        quakeT.color(turtle_color_r, turtle_color_g, turtle_color_b)

        for akey in eqClusters[clusterIndex]:
            lon = eqDict[akey][0]
            lat = eqDict[akey][1]
            mag = eqDict[akey][2]
            quakeT.goto(lon * wFactor, lat * hFactor)
            quakeT.dot(mag * 1.8)  # increases with magnitude
    #
    quakeWin.exitonclick()


visaulizeQuakes("earthquakes.csv", 25)
