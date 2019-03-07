"""
Earthquake Watch
CIS 210 W19 Project #

Author: [Jacob Rammer]

Credits: [N/A]

Graphing earthquakes with turtle graphics
"""
from math import sqrt
import random
from turtle import *
import turtle


def readFile(fileName="Demo.txt"):
    """(str) -> dict"""

    # datadict = {}
    #
    # with open("earthquakes.csv") as equake_date:
    #     equake_date.readline()

    datafile = open(fileName, "r")
    datadict = {}

    key = 0

    for aline in datafile:
        items = aline.split()
        key = key + 1
        lat = float(items[3])
        lon = float(items[4])

        datadict[key] = [lon, lat]

    return datadict

# readFile()


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
        rkey = random.randint(1, len(datadict))
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


def visaulizeQuakes(dataFile, k=6, r=7):  # using values from book

    datadict = readFile(dataFile)
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)

    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap1800_900.gif")
    quakeWin.screensize(1800, 900)

    wFactor = (quakeWin.screensize()[0] / 2) / 180
    hFactor = (quakeWin.screensize()[1] / 2) / 90

    quakeT.hideturtle()
    quakeT.up()

    turtle_color_r = random.random()
    turtle_color_g = random.random()
    turtle_color_b = random.random()

    colorlist = ["red", "black", "blue", "orange", "cyan", "yellow"]

    for clusterIndex in range(k):
        quakeT.color(colorlist[clusterIndex])
        for akey in clusters[clusterIndex]:
            lon = datadict[akey][0]
            print("lon", lon)
            lat = datadict[akey][1]
            print("lat", lat)
            quakeT.goto(lon*wFactor, lat * hFactor)
            quakeT.dot()
    #
    quakeWin.exitonclick()

    return None


visaulizeQuakes("Demo.txt")
