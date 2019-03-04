def isMember(aseq, target):

    if type(aseq) == list:
        aseq.sort()
    if len(aseq) == 0:
        return False

    left_val = 0
    right_val = len(aseq)

    while right_val > left_val:

        mid_point = (left_val + right_val) // 2
        length = len(aseq[left_val:right_val])
        # print(length)

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
    print(isMember((1, 2, 3, 3, 4), 4))
    print(isMember((1, 2, 3, 3, 4), 2))
    print(isMember('aeiou', 'i'))
    print(isMember('aeiou', 'y'))
    print(isMember((1, 3, 5, 7), 4))
    print(isMember((23, 24, 25, 26, 27), 5))
    print(isMember((0, 1, 4, 5, 6, 8), 4))
    print(isMember((0, 1, 2, 3, 4, 5, 6), 3))
    print(isMember((1, 3), 1))
    print(isMember((2, 10), 10))
    print(isMember((99, 100), 101))
    print(isMember((42,), 42))
    print(isMember((43,), 44))
    print(isMember((), 99))


main()
