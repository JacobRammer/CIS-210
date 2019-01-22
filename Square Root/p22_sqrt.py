"""
CIS 210 STYLE
CIS 210 W19 Project 2-2

Author: [Jacob Rammer]

Credits: [N/A]

# TODO desc
"""


def main():
    pass


def mysqrt(n, k):
    pass


def sqrt_compare(num, iterations):
    pass


def test(n, k):
    x1 = n / k
    average = (k + x1) / 2

    for i in range(k):
        x2 = n / average
        average2 = (average + x2) / 2

    return average2


print(test(25, 5))
