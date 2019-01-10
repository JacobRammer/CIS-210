'''                          # FILE HEADER
Nature's Thermometer: Cricket Chirps.
CIS 210 W19 Project 1

Author: [Jacob Rammer]

Credits: [N/A]

Determine the temperature based on cricket
chirps. (Farmers Almanac)
'''


def chirps_to_ctemp(ch25):  # FUNCTION HEADER
    '''(int) -> float       #TYPE CONTRACT
                            #BRIEF DESCRIPTION refers to
                            #PARMS, RETURN VAL
    Return celsius temp estimated based on
    number of cricket chirps in a 25 second
    interval (ch25) - divide by 3 and add 4
    to get the celsius temperature.
                            #EXAMPLES OF USE
    >>> chirps_to_ctemp(48)
    20.0
    >>> chirps_to_ctemp(93)
    35.0
    >>> chirps_to_ctemp(0)
    4.0
    '''

    temp = (ch25 / 3) + 4

    return temp


def chirps_to_ftemp(ch14):
    '''(int) -> int

    Return fahrenheit temp estimated based on
    number of cricket chirps in a 14 second
    interval (ch14) - add 40.

    >>> chirps_to_ftemp(0)
    40
    >>> chirps_to_ftemp(50)
    90
    '''

    temp = ch14 + 40

    return temp
