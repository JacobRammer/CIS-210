"""
CIS 210 Majors
CIS 210 W19 Project #

Author: [Jacob Rammer]

Credits: [N/A]

Analyze the different majors in CIS 210
"""


def majors_readf(fname):
    """(string) -> list

    Open a file as fname and create a list with data starting from line 3, returning the list.

    i_am_a_file.txt
    line 1
    line 2
    cis
    math

    artist.txt
    line 1
    line 2
    Architects
    Breaking Benjamin

    # doctests will not work

    > majors_readf("i_am_a_file.txt")
    ["cis", "math"]

    > majors_readf("artist.txt")
    ["Architects", Breaking Benjamin]

    """
    majors_list = []

    with open(fname) as majors_data:
        majors_data.readline()
        majors_data.readline()

        for line in majors_data:
            major = line.strip()
            majors_list.append(major)

    return majors_list


def majors_analysis(majorsli=majors_readf("majors_cis210w19.txt")):
    """(list) -> list, int

    Create a dictionary from each line of a text file. If the line is already in the dictionary as a key, add 1 to
    its value. Find the largest occurrence and assign it to largest_major, then loop through dict. to check to see
    if keys have same values. Give parameter default argument so I don't have to keep typing it.
    Returns the major with most occurrences and length of majors_dict (only counting majors once).

    >>> majors_analysis()
    (['CIS'], 23)

    >>> majors_analysis(["cis", "cis", "math"])
    (['cis'], 2)

    """
    majors_dict = {}

    for i in majorsli:
        if i not in majors_dict:
            majors_dict[i] = 1
        else:
            majors_dict[i] += 1

    largest_major = max(majors_dict.values())
    majors_mode = [m for m, v in majors_dict.items() if v == largest_major]

    return majors_mode, len(majors_dict)


def majors_report(majors_mode, majors_ct, majorsli):
    """(list, int, list) -> None

    Print the report of the analysis of majors. Check to see if arguments are passed to the function, if not
    use the return value tuple from majors_analysis. Calls frequencyTable to print table. Returns None

    >>> majors_report(["cis", "idk"], 2, ["cis", "cis", "idk", "idk"])
        2 majors are represented in CIS 210 this term.
        The most represented major(s): cis idk
        <BLANKLINE>
        ITEM FREQUENCY
        cis     2
        idk     2

        >>> majors_report(['CIS', 'EXPL'], 3, ['CIS', 'CIS', 'EXPL','COLT', 'EXPL'])
        3 majors are represented in CIS 210 this term.
        The most represented major(s): CIS EXPL
        <BLANKLINE>
        ITEM FREQUENCY
        CIS     2
        COLT    1
        EXPL    2

    """

    print(majors_ct, "majors are represented in CIS 210 this term.")
    print("The most represented major(s): ", end='')

    for i in majors_mode:
        print("".join(i), end=' ')

    print("\n")

    majorsli_v2 = frequencyTable(majorsli)

    return None


def genFrequencyTable(alist):
    """(list) dict.

    This function iterates over every item in alist and adds them to a dictionary as a key (countDict) if it is their
    first occurrence. If the item is already a key in countDict, add one to the occurrence count (which starts at 1).
    Return the dictionary.

    >>> genFrequencyTable([13, 18, 13, 14, 13, 16, 14, 21, 13])  # simple
    {13: 4, 18: 1, 14: 2, 16: 1, 21: 1}
    >>> genFrequencyTable([0])  # edge
    {0: 1}

    """
    countDict = {}

    for item in alist:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1

    return countDict


def frequencyTable(alist):
    """(list) -> None

    Given a list, this function will find the total number of occurrences of each item in the list. Returns none.

    > frequencyTable([1, 2, 3, 4])  # simple
    ITEM    FREQUENCY
    1       1
    2       1
    3       1
    4       1
    > frequencyTable([1])  # edge - 1
    ITEM    FREQUENCY
    1       1

    """

    countDict = genFrequencyTable(alist)

    itemlist = list(countDict.keys())
    itemlist.sort()

    print("ITEM", "FREQUENCY")

    for item in itemlist:
        print(item.ljust(7), countDict[item])

    return None


def main():
    '''()-> None
    Calls: majors_readf, majors_analysis, majors_report
    Top level function for analysis of CIS 210 majors data.
    '''

    fname = 'majors_cis210w19.txt'

    majorsli = majors_readf(fname)  # read
    majors_mode, majors_ct = majors_analysis(majorsli)  # analyze
    majors_report(majors_mode, majors_ct, majorsli)  # report
    return None

main()
# print(majors_analysis())
