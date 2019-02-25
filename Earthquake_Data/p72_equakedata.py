"""
Earthquake Data
CIS 210 W19 Project #

Author: [Jacob Rammer]

Credits: [N/A]

Analyzing earthquake data
"""
import p51_data_analysis as p51


# completed challenge

def equake_readf(fname):
    """(str) -> list

    Open a text file, skipping the header and recording th e magnitude of earthquakes over a certain period of time.
    Return the list of earthquake magnitudes


    Non working examples of use

    file.txt
    2010-07-28T16:12:05.610Z,43.756,-125.815,10,5.2,mwc,193,143.9,,0.93,us,usp000hh0t,2017-08-01T16:34:36.951Z,"off the coast of Oregon",earthquake,,,,,reviewed,us,gcmt

    file2.txt
    2010-07-28T16:12:05.610Z,43.756,-125.815,10,5.2,mwc,193,143.9,,0.93,us,usp000hh0t,2017-08-01T16:34:36.951Z,"off the coast of Oregon",earthquake,,,,,reviewed,us,gcmt
    1993-12-04T22:15:19.720Z,42.2915,-122.0086667,4.797,5.1,md,126,113,,0.11,uw,uw10316468,2017-04-13T22:06:07.852Z,"Oregon",earthquake,0.468,0.56,0.04,7,reviewed,uw,uw

    > equake_readf("file.txt")
    [5.2]

    > equake_readf("file2.txt")
    [5.2, 5.1]

    """
    magnitude_list = []

    with open(fname) as equake_data:
        equake_data.readline()  # skip header line

        for line in equake_data:  # magnitude is 5th value
            magnitude = line.split(",")[4]
            magnitude_list.append(float(magnitude))

    return magnitude_list


def equake_analysis(magnitudes):
    """(list) -> (num, num, num)

    Find the mean, median, mode of a list of earthquake magnitudes. Return the calculations as a tuple


    >>> equake_analysis([5.0, 2.3, 2.0, 2.0, 4.0])
    (3.06, 2.3, [2.0])

    >>> equake_analysis([5.0, 2.3, 2.0, 2.0, 4.0, 5.0, 2.3, 2.0, 2.0, 4.0])
    (3.06, 3.4499999999999997, [2.0])

    """

    mean = p51.mean(magnitudes)
    median = p51.median(magnitudes)
    mode = p51.mode(magnitudes)

    return mean, median, mode


def equake_report(mmm, magnitudes):  # mmm: mean, median, mode
    """(tuple, list) -> None

    Unpack the tuple with the mean, median, mode calculations and print the statistics and frequency table
    of the earthquake date from the text file. Returns none.

    >>> equake_report((3.06, 3.4499999999999997, [2.0]), [5.0, 2.3, 2.0, 2.0, 4.0, 5.0, 2.3, 2.0, 2.0, 4.0]) #doctest: +NORMALIZE_WHITESPACE
    Earthquake Data Analysis
    100 Years Ago to Present
    250km Centered at Eugene, OR
    <BLANKLINE>
    There have been 10 earthquakes over the past 100 years.
    <BLANKLINE>
    Mean magnitude is: 3.06
    Median magnitude is: 3.4499999999999997
    Mode(s) of magnitudes is: [2.0]
    <BLANKLINE>
    ITEM FREQUENCY
    2.0     4
    2.3     2
    4.0     2
    5.0     2

    >>> equake_report((3.06, 2.3, [2.0]), [5.0, 2.3, 2.0, 2.0, 4.0]) #doctest: +NORMALIZE_WHITESPACE
    Earthquake Data Analysis
    100 Years Ago to Present
    250km Centered at Eugene, OR
    <BLANKLINE>
    There have been 5 earthquakes over the past 100 years.
    <BLANKLINE>
    Mean magnitude is: 3.06
    Median magnitude is: 2.3
    Mode(s) of magnitudes is: [2.0]
    <BLANKLINE>
    ITEM FREQUENCY
    2.0     2
    2.3     1
    4.0     1
    5.0     1

    """

    mean, median, mode = mmm

    print("Earthquake Data Analysis", "\n100 Years Ago to Present\n250km Centered at Eugene, OR\n")
    print("There have been", len(magnitudes), "earthquakes over the past 100 years.\n")
    print("Mean magnitude is:", mean, "\nMedian magnitude is:", median, "\nMode(s) of magnitudes is:", mode, "\n")

    p51.frequencyTable(magnitudes)

    return None


def main():
    '''()-> None
    Calls: equake_readf, equake_analysis, equake_report
    Top level function for earthquake data analysis.
    Returns None.
    '''

    fname = 'equakes25f.txt'
    # fname = 'equakes50f.txt'

    emags = equake_readf(fname)
    mmm = equake_analysis(emags)
    equake_report(mmm, emags)
    return None


main()
