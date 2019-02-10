"""
Data Analysis
CIS 210 W19 Project 5-1

Author: [Jacob Rammer]

Credits: [N/A]

Data analysis using lists and dictionaries
"""


def isEven(n):
    """(int) -> bool

    Check to see if the length of a list is even. Return True if even, false if odd.

    >>> isEven(100)  # simple
    True
    >>> isEven(len([5]))  # edge
    False

    """

    if n % 2 == 0:
        return True
    else:
        return False


def genFrequencyTable(alist):
    """(list) dict.

    This function iterates over every item in alist and adds them to a dictionary as a key if it is their first
    occurrence. If the item is already a key in countDict, add one to the occurrence count (which starts at 1). Return
    the dictionary.

    >>> genFrequencyTable([13, 18, 13, 14, 13, 16, 14, 21, 13])  # simple
    {13: 4, 18: 1, 14: 2, 16: 1, 21: 1}
    >>> genFrequencyTable([0])
    {0: 1}

    """
    countDict = {}

    for item in alist:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1

    return countDict


def mean(alist):
    """(list) -> Float

    Find the mean of a list, and return the value.

    >>> mean([1, 1, 2, 2, 2, 3, 4, 5])  # simple
    2.5
    >>> mean([13, 18, 13, 14, 13, 16, 14, 21, 13])  # simple
    15.0
    >>> mean([0, 0, 0, 0, 0, 0])  # edge
    0.0

    """
    mean = sum(alist) / len(alist)

    return mean


def median(alist):
    """(list) -> Number

    Find the media of a list. Call isEven to check to see if the length of the list is even, and execute to function
    based on the returned value. Return the median of the list.

    >>> median([13, 18, 13, 14, 13, 16, 14, 21, 13])  # simple
    14
    >>> median([0])  # edge
    0

    """

    copylist = alist[:]  # make a copy using the slice operator
    copylist.sort()

    if isEven(len(copylist)):
        rightmid = len(copylist) // 2
        leftmid = rightmid - 1
        median = (copylist[leftmid] + copylist[rightmid] / 2)

    else:
        mid = len(copylist) // 2
        median = copylist[mid]

    return median


def mode(alist):
    """(list) -> list

    Find the mode of a list. Iterate over every item in the list and add it as a key and start the occurrence at 1.
    If the key already exists, add 1 to the occurrence. Only finds mode if there are repeats. Returns the mode list.

    >>> mode ([13, 18, 13, 14, 13, 16, 14, 21, 13])  # simple
    [13]
    >>> mode([0, 1, 2, 3, 4])  # edge (no repeats)
    []


    """

    countDict = genFrequencyTable(alist)

    countlist = countDict.values()
    maxcount = max(countlist)

    modelist = []

    for item in countDict:
        if countDict[item] == maxcount and countDict[item] > 1:
            modelist.append(item)

    return modelist


def frequencyTable(alist):
    """(list) -> None

    Given a list, this function will find the total number of occurrences of each item in the list. Returns none.

    > frequencyTable([1, 2, 3, 4])  # simple
    ITEM    FREQUENCY
    1       1
    2       1
    3       1
    4       1
    > frequencyTable([1])  # edge
    ITEM    FREQUENCY
    1       1

    """

    countDict = genFrequencyTable(alist)

    itemlist = list(countDict.keys())
    itemlist.sort()

    print("ITEM", "FREQUENCY")

    for item in itemlist:
        print(item, "   ", countDict[item])

    return None


def main():
    """p51 program driver"""

    equakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3,
               2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6,
               4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1,
               4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9,
               2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7,
               4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7,
               3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1,
               2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1,
               2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3,
               6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
               2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
               2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9,
               4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5,
               4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6,
               2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1,
               2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1,
               2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5,
               4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1,
               4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0,
               2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
               3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5,
               2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
               2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7,
               2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6,
               2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9,
               2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1,
               3.1, 4.6, 2.8, 3.1, 6.3]
    frequencyTable(equakes)
    print(mean(equakes))
    print(median(equakes))
    print(mode(equakes))


main()
