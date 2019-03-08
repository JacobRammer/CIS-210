"""
Earthquake Watch
CIS 210 W19 Project 9-1

Author: [Jacob Rammer]

Credits: [Python Programming in Context]

Graphing earthquakes with turtle graphics
"""
from math import sqrt
from random import randint
import turtle


def readFile(fileName="earthquakes.csv"):  # TODO change for class file
    """(str) -> dict

    Get the magnitude, longitude, and latitude from a file. Return the dictionary containing the information.

    Doctest will not work due to file randomness

    > readFile("earthquakes.csv")
    {1: [-178.006, -30.5749, 5.4]}

    """

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


def euclidD(point1, point2):
    """(list, list) -> float

    Measure the distance between two points - the longitude / latitude value - using Euclidean distance. Return the
    Euclidean distance calculation.

    >>> euclidD([-178.006, -30.5749], [159.5408, -53.4107])
    338.3183647866015
    >>> euclidD([120.4262, 18.6004], [146.9481, 41.9336])
    35.32491191567222

    """

    total = 0

    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total = total + diff

    euclidDistance = sqrt(total)

    return euclidDistance


def createCentroids(k, datadict):
    """(int, dict) -> list

    Using the k-means cluster, choose k random points from datadict to be used as centroids centroids. Cannot use same
    point twice. Return the list of centroids.

    Doctest will not work due to randomness

    > createCentroids(2, {1: [-178.006, -30.5749, 5.4], 2: [-72.6378, -33.664, 5.5]}
    [[178.006, -30.5749, 5.4], 2: [-72.6378, -33.664, 5.5]]
    > createCentroids(1, {1: [-178.006, -30.5749, 5.4], 2: [-72.6378, -33.664, 5.5], 3: [120.4262, 18.6004, 5.6]}
    [[120.4262, 18.6004, 5.6]]

    """

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
    """(int, list, dict, int) -> list

    Create a list of clusters in relations to the closest centroid created in createCentroids. Distance is found using
    the Euclidean distance calculations from euclidD. K is number of clusters, repeats is number of time to analyze data
    Return the list of clusters.

    Non working doc test due to file randomness

    > createClusters(1, [[-178.006, -30.5749, 5.4]], {1: [-178.006, -30.5749, 5.4]}, 1) #doctest: +NORMALIZE_WHITESPACE
    **** PASS 0 ****
    CLUSTER
    [-178.006, -30.5749, 5.4]
    [[1]]

    > createClusters(2, [[159.5408, -53.4107, 5.8], [-70.1267, -14.6844, 7.0]], {1: [-70.1267, -14.6844, 7.0], 2: [159.5408, -53.4107, 5.8]}, 2) #doctest: +NORMALIZE_WHITESPACE
    **** PASS 0 ****
    CLUSTER
    [159.5408, -53.4107, 5.8]
    CLUSTER
    [-70.1267, -14.6844, 7.0]
    **** PASS 1 ****
    CLUSTER
    [159.5408, -53.4107, 5.8]
    CLUSTER
    [-70.1267, -14.6844, 7.0]
    [[2], [1]]

    """

    for apass in range(repeats):
        # print("**** PASS", apass, "****")
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

        # comment out per project spec

        # for c in clusters:
        #     print("CLUSTER")
        #     for key in c:
        #             print(datadict[key], end=" ")
        #     print()

    return clusters


def change_turtle_color():  # each cluster gets own color
    """() -> tuple

    Generate random color decimal codes for turtle plotting. Auxiliary function created because there can be k clusters.
    Returns the RGB decimal code tuple.

    Doctest will not work due to randomness

    > change_turtle_color()
    (100, 150, 255)
    > change_turtle_color()
    (255, 255, 0)

    """
    turtle_color_r = randint(0, 255)
    turtle_color_g = randint(0, 255)
    turtle_color_b = randint(0, 255)

    return turtle_color_r, turtle_color_g, turtle_color_b


def visaulizeQuakes(dataFile, k, r):
    """(str, int, int) -> None

    Create variable needed to plot earthquake date with Turtle. Create the data dictionary by calling readFile,
    create centroids, and clusters by calling the appropriate functions. K = clusters, r = repeats. Returns none

    """

    datadict = readFile(dataFile)
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)

    eqDraw(k, datadict, clusters)  # plotting points

    return None


def eqDraw(k, eqDict, eqClusters):
    """(int, dict, list) -> None

    Initialize turtle objects. Plot earthquakes on the map using turtle by looping through the eqDict.
    Their occurrence will be graphed by a dot on the map with a size of 1.8 times their magnitude. Returns none

    """

    quakeT = turtle.Turtle()
    turtle.colormode(255)
    quakeT.speed("fastest")
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap1800_900.gif")
    quakeWin.screensize(1800, 900)

    wFactor = (quakeWin.screensize()[0] / 2) / 180  # coordinate calculations for longitude
    hFactor = (quakeWin.screensize()[1] / 2) / 90  # coordinate calculations for latitude

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

    quakeWin.exitonclick()

    return None


def main():
    """program driver for 9-1"""

    # k and v must be less than number of earthquakes
    k = 6  # clusters
    r = 7
    visaulizeQuakes("earthquakes.csv", k, r)


main()
