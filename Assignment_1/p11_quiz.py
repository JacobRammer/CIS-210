'''
CIS 210 STYLE
CIS 210 W19 Project 1-1

Author: [Jacob Rammer]

Credits: [N/A]

Add docstrings to Python functions that implement quiz 1 pseudocode.
(See p11_cricket for examples of functions with docstrings.)
'''


def q1(onTime, absent):
    ''' (bool) -> str

    return greeting string based on bool value

    >>> q1(True, False)
    returns: "Hello"

    >>> q1(False, False)
    returns: "Better late than never"
    '''

    if onTime:
        return 'Hello!'
    elif absent:
        return 'Is anyone there?'
    else:
        return 'Better late than never.'


def q2(age, salary):
    '''(number) -> bool

    Checks to see if individual is classified as dependant
    Returns True if under 18 and salary is less than 10,000
    Else: False

    >>> print(q2(17, 5000))
    True
    >>> print(q2(17, 50000))
    False
    '''

    return (age < 18) and (salary < 10000)


def q3():
    ''' (No arg) -> int

    Evaluates the value of variables and assigns result based
    on evaluation and returns result

    #  When ran: result will now be equal to 6
    >>> q3()
    6
    '''

    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result


def q4(balance, deposit):
    ''' (Number) -> Number

    Loops through and adds the deposit value 10 times to the balance
    and returns the balance of the account

    >>> print(q4(100, 10))
    200
    >>> print(q4(100, 1))
    110
    '''

    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance


def q5(nums):
    ''' (list) -> int

    if list nums is greater than 0 and list item is positive,
    loop through and increment i until i is greater than list
    nums and return incremented result var

    >>> int(q5([-5, 6])
    1
    >>> print(q5([5, 6, 9999999999]))
    3
    '''

    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result


def q6():
    '''(No arg) -> int

    multiply p by 2 on each loop and re-assign result.
    Returns the final value of p

    # After running: p = 16
    >>> q6()
    16
    '''

    i = 0
    p = 1
    while i < 4:

        # bug is here. assigns i to 1 on every loop, creating an infinite loop
        # i = 1
        p = p * 2
        i += 1

    return p
