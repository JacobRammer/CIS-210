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

    There are three test cases for this function. Case 1 is executed if test input matches up with test output.
    Since checkTone has a side effect print statement, it has it own test case, so the output matches up with the
    project specifications. Case 3 is if test case input / output does not match and prints expected output. Since there
    are two functions that do the same thing, wrote if statements to check the name of the function and execute
    accordingly. Successfully implemented challenge by commenting out print statements and adding pass to if statements.

    >>> test_decode(ps4.checkTone)

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
    testCases = (
        ('lohi', True),
        ('hajeku', True),
        ('olih', False),
        ('', False),
        ('z', False),
        ('zz', False),
        ('ddpe', True)
    )

    if f.__name__ == "checkTone":
        for i, o in testCases:
            if ps4.checkTone(i):  # case 1
                print("Checking", f.__name__, "('" + i + "')...", end='')
                print("The value", o, "is correct!\n")
                # pass

            elif ps4.checkTone(i) == o:  # case 2
                print("Checking", f.__name__, "('" + i + "')...", end='')
                print("The value", o, "is correct!\n")

            else:  # case 3
                print("('" + i + "')...", end='')
                print("The value", o, "is incorrect!\n")

    elif f.__name__ == "checkTone2":
        for i, o in testCases:
            if ps4.checkTone(i):  # case 1
                print("Checking", f.__name__, "('" + i + "')...", end='')
                print("The value", o, "is correct!\n")
                # pass

            elif ps4.checkTone(i) == o:  # case 2
                print("Checking", f.__name__, "('" + i + "')...", end='')
                print("The value", o, "is correct!\n")

            else:  # case 3
                print("('" + i + "')...", end='')
                print("The value", o, "is incorrect!\n")

    return None


test_checkTone(ps4.checkTone)
