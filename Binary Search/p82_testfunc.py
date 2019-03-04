"""
Testing binary search
CIS 210 W19 Project 8-2

Author: [Jacob Rammer]

Credits: [N/A]

Binary search test functions
"""
import p81_binsearch as p81

def test_isMember():
    """() -> None

    Test binary search using a pre-defined tuple list looping through the values. Returns none.


    > test_isMember()
    <report results>

    """

    test_cases = (
        ((1, 2, 3, 3, 4), 4, True),
        ((1, 2, 3, 3, 4), 2, True),
        ('aeiou', 'i', True),
        ('aeiou', 'y', False),
        ((1, 3, 5, 7), 4, False),
        ((23, 24, 25, 26, 27), 5, False),
        ((0, 1, 4, 5, 6, 8), 4, True),
        ((0, 1, 2, 3, 4, 5, 6), 3, True),
        ((1, 3), 1, True),
        ((2, 10), 10, True),
        ((99, 100), 101, False),
        ((42,), 42, True),
        ((43,), 44, False),
        ((), 99, False),
        ("aeiouy", "u", True),  # added
        ("python", "o", True),  # added
    )

    for seq, tar, res in test_cases:
        if p81.isMember(seq, tar) == res:
            print("Checking", seq, "for target", str(tar) + "... its value", res, "is correct!")
        else:
            print("Checking", seq, "for target", str(tar) + "... its value", res, "is incorrect! Expected",
                  p81.isMember(seq, tar))

    return None


def main():
    """p82 project driver"""

    test_isMember()


main()
