def reverse_int(n):
    """(int) -> str

    Reverse a integer and return the reversed string

    >>> reverse_int(123)
    '321'
    >>> reverse_int(1234)
    '4321'

    """

    if n < 10:
        return str(n)
    r = n % 10
    q = n // 10

    return str(r) + reverse_int(q)


def isPal(s):
    """(str) -> bool

    Check s to see if it is a palindrome. Return true if it is, else false

    >>> isPal("abba")
    True
    >>> isPal("qwerty")
    False

    """

    if len(s) == 1:
        return True
    elif len(s) == 0:
        return False
    q = s[0] == s[-1]
    c = isPal(s[1:-1]) == q
    return q and c


print(isPal(""))
