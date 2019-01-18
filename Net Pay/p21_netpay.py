"""
Net pay calculator
CIS 210 W19 Project 2-1

Author: [Jacob Rammer]

Credits: [N/A]

Calculate the net pay for an employee
using the hours worked and tax deducted
"""


def main():
    """Net pay program driver"""

    print("For 10 hours work, netpay is:", netpay(10))
    print("For 40 hours work, netpay is:", netpay(40))

    return None


def tax(gross):
    """ (Number) -> Float

    Calculate the tax based gross pay using
    a TAX_RATE of 15 percent by multiplying gross and tax rate,
    return net pay

    >>> tax(100)
    913.75
    >>> tax(46)
    420.32
    """

    TAX_RATE = .15

    net_pay = gross * TAX_RATE

    return net_pay


def netpay(hours):
    """ (Number) -> Float

    Calculate the gross_pay based on hourly_rate
    and hours worked. Then call tax() to deduct
    tax rate and return net pay for pay period
    rounded to two decimal places.

    >>> netpay(1)
    9.14
    >>> netpay(41)
    374.64
    """

    HOURLY_RATE = 10.75

    gross_pay = (hours * HOURLY_RATE)
    net_pay = gross_pay - tax(gross_pay)

    return round(net_pay, 2)


main()
