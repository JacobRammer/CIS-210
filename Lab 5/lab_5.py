def findlast(s, ch):
    '''(str, str) -> int
    return position of last occurrence of ch s,
    or -1 if ch does not occur in s

    >>> findlast('mississippi', 'm')
    0
    >>> findlast("hello", "o")
    4
    >>> findlast("qwerty", "p")
    -1

    >>> findlast("", "p")
    -1
    >>> findlast("hello", "l")
    3

    >>> findlast("hello", "he")
    -1

    >>> findlast("hello", "")
    -1

    '''

    lastpos = -1

    if len(ch) == 1 and isinstance(ch, str):
        for idx in range(len(s)):
            if s[idx] == ch:
                lastpos = idx

    return lastpos

