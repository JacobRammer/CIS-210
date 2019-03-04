def isMember(aseq=[0,1,2,3,4,5,6], target=2):

    aseq.sort()

    mid = len(aseq) / 2
    print(mid)
    if target == mid:
        return True
    elif target < mid:
        pass

    # first = 0
    # last = len(aseq) - 1
    # mid = (first + last) // 2
    # print(mid)


print(isMember())
