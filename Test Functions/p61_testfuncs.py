"""
# TODO Title
CIS 210 W19 Project #

Author: [Jacob Rammer]

Credits: [N/A]

# TODO Description
"""
import p41_alphapin_key as ps4


def test_decode(f):
    """(function) -> None

    This function tests the results outputted from either alphapinDecode or alphapinDecode2 functions.
    There are three test cases for this function. Case 1 is executed if test input matches up with test output from
    testCases Since checkTone has a side effect print statement, it has it own test case, so the output matches up with
    the project specifications. Case 3 is if test case input / output does not match and prints expected output. Since
    there are two functions that do the same thing, wrote if statements to check the name of the function and execute
    accordingly. Successfully implemented challenge by commenting out print statements and adding pass to if statements.
    Left commented prints just in case. Returns none.

    Only applicable test case for function. NOTE: if TestCases changes, doctest may fail

    >>> test_decode(ps4.alphapinDecode) #doctest: +NORMALIZE_WHITESPACE
    Checking alphapinDecode ('bomelela')...The value 34641400 is incorrect! Expected 3464140
    <BLANKLINE>
    Checking alphapinDecode ('dijucee')...Tone is not in correct format.
    The value 123465 is incorrect! Expected -1
    <BLANKLINE>

    """
    testCases = (
        ('lo', 43),
        ('hi', 27),
        ('bomelela', 34641400),  # added
        ('bomelela', 3464140),
        ('bomeluco', 3464408),
        ('', -1),
        ('abcd', -1),
        ('diju', 1234),
        ('dijucee', 123465),  # added
    )

    if f.__name__ == "alphapinDecode":  # since there are two decode functions
        for i, o in testCases:
            if ps4.checkTone(i) and ps4.alphapinEncode(o) == i:  # case 1
                # print("Checking", f.__name__, "('" + i + "')...", end='')
                # print("The value", o, "is correct!\n")
                pass

            elif not ps4.checkTone(i) and not ps4.alphapinEncode(o):  # case 2
                # print("Checking", f.__name__, "('" + i + "')...", end='')
                # print("The value", o, "is correct!\n")
                pass

            else:  # case 3
                print("Checking", f.__name__, "('" + i + "')...", end='')
                print("The value", o, "is incorrect!", "Expected", ps4.alphapinDecode(i), "\n")

    elif f.__name__ == "alphapinDecode2":  # since there are two decode functions
        for i, o in testCases:
            if ps4.checkTone(i) and ps4.alphapinEncode(o) == i:  # case 1
                # print("Checking", f.__name__, "('" + i + "')...", end='')
                # print("The value", o, "is correct!\n")
                pass

            elif not ps4.checkTone(i) and not ps4.alphapinEncode(o):  # case 2
                # print("Checking", f.__name__, "('" + i + "')...", end='')
                # print("The value", o, "is correct!\n")
                pass

            else:  # case 3
                print("Checking", f.__name__, "('" + i + "')...", end='')
                print("The value", o, "is incorrect!", "Expected", ps4.alphapinDecode(i), "\n")

    return None


# test_decode(ps4.alphapinDecode2)


def test_checkTone(f):
    """(function) -> None

    This function tests the results outputted from either checkTone or checkTone2 functions.
    If expected results are received, nothing is printed and loop moved onto next function. Per the project challenge.
    If expected output or input from testCases is wrong, print expected results. Since there are two checkTone
    functions, check the name of the function to properly test results. Left commented prints just in case.
    Returns none.

    Only applicable test case for function. NOTE: if TestCases changes, doctest may fail

    >>> test_decode(ps4.alphapinDecode) #doctest: +NORMALIZE_WHITESPACE
    Checking alphapinDecode ('bomelela')...The value 34641400 is incorrect! Expected 3464140
    <BLANKLINE>
    Checking alphapinDecode ('dijucee')...Tone is not in correct format.
    The value 123465 is incorrect! Expected -1
    <BLANKLINE>
    """
    testCases = (
        ('lohi', True),
        ('hajeku', True),
        ('olih', False),
        ('', False),
        ('z', False),
        ('zz', False),
        ('ddpe', True)  # added
    )

    if f.__name__ == "checkTone":  # since there are two checkTone functions
        for i, o in testCases:
            if ps4.checkTone(i) == o:  # case 1
                # print("Checking", f.__name__, "('" + i + "')...", end='')
                # print("The value", o, "is correct!\n")
                pass

            else:  # case 2
                print("Checking", f.__name__, "('" + i + "')...", end='')
                print("The value", o, "is incorrect!", "Expected", ps4.checkTone(i), "\n")

    elif f.__name__ == "checkTone2":  # since there are two checkTone functions
        for i, o in testCases:
            if ps4.checkTone(i) == o:  # case 1
                # print("Checking", f.__name__, "('" + i + "')...", end='')
                # print("The value", o, "is correct!\n")
                pass

            else:
                print("Checking", f.__name__, "('" + i + "')...", end='')
                print("The value", o, "is incorrect!", "Expected", ps4.checkTone2(i), "\n")

    return None


# test_checkTone(ps4.checkTone2)

def main():
    """Program driver"""

    test_decode(ps4.alphapinDecode)
    test_decode(ps4.alphapinDecode2)
    test_checkTone(ps4.checkTone)
    test_checkTone(ps4.checkTone2)


main()
