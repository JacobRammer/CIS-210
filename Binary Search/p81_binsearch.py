"""
Binary Search
CIS 210 W19 Project 8-1

Author: [Jacob Rammer]

Credits: [N/A]

Search a sequence using binary search
"""


def isMember(aseq, target):
    """(sequence, item) -> bool

        Perform a binary search on aseq. Aseq can be a list, tuple, string, etc. Target is a single element that is being
        searched for. If aseq is a list, sort it, and if it is empty, return false. Compare the midpoint to target and
        depending on the evaluation, left_val and right_val will be adjusted accordingly to halve aseq. If aseq is not a
        list, the sequence will need to be sorted in the argument. Returns true or False depending on if the target is
        in aseq.

        >>> isMember((0, 1, 2, 3), 0)
        True
        >>> isMember("qwerty", 'y')
        True
        >>> isMember([], 0)
        False

        """

    if type(aseq) == list:
        aseq.sort()
    if len(aseq) == 0:
        return False

    left_val = 0
    right_val = len(aseq)

    while right_val > left_val:

        mid_point = (left_val + right_val) // 2
        length = len(aseq[left_val:right_val])

        if target == aseq[mid_point]:
            return True
        elif length == 1:
            break
        elif target < aseq[mid_point]:
            right_val = mid_point
        elif target > aseq[mid_point]:
            left_val = mid_point

    return False


def main():
    """p81 project driver"""

    isMember((1, 2, 3, 3, 4), 4)
    isMember((1, 2, 3, 3, 4), 2)
    isMember('aeiou', 'i')
    isMember('aeiou', 'y')
    isMember((1, 3, 5, 7), 4)
    isMember((23, 24, 25, 26, 27), 5)
    isMember((0, 1, 4, 5, 6, 8), 4)
    isMember((0, 1, 2, 3, 4, 5, 6), 3)
    isMember((1, 3), 1)
    isMember((2, 10), 10)
    isMember((99, 100), 101)
    isMember((42,), 42)
    isMember((43,), 44)
    isMember((), 99)


main()
