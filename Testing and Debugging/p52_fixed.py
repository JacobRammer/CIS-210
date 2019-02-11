"""
# TODO Title
CIS 210 W19 Project #

Author: [Jacob Rammer]

Credits: [N/A]

# TODO Description
"""
import doctest


def bigSalesBug(sales_list):
    """(list) -> number

    Returns sum of all sales for amounts at or over $40,000.
    sales_list has the record of all the sales.

    >>> bigSalesBug([40000, 45.67, 19000.0, 25000, 100000])
    140000.0

    """

    total = 0.00
    for sales in sales_list:
        if sales >= 40_000:  # missing : and >=
            total += sales  # typo

    return total  # return indented


def ratsBug(weight, rate):
    """(number, number) -> tuple

    Return number of weeks it will
    take for a rat to weigh 1.5 times
    as much as its original weight
    (weight > 0) if it gains at rate (rate > 0).

    >>> ratsBug(10, .1)
    (16.1, 5)

    """

    weeks = 0
    oldWeight = weight  # needed because the while loop was re-assigning a value to weight on each pass.

    while weight <= (1.5 * oldWeight):  # changed from weight to oldWeight
        weight += weight * rate
        weeks += 1

    return round(weight, 1), weeks  # removed (), not needed. Moved round to return statement


def my_averageBug(dataset):
    """(list of numbers) -> float

    returns average of values in dataset,
    but zeros do not count at all

    >>> my_averageBug([2, 3])
    2.5
    >>> my_averageBug([2, 0, 3])
    2.5
    """
    count = 0
    total = 0
    for value in dataset:
        if value != 0:  # removed '', values not a string
            total += value
            count += 1  # moved count to if statement

    avg = total / count

    return avg


def countSeqBug(alist):
    """(list) -> int

    Returns the length of the longest recurring
    sequence in alist, a list of strings.

    While this is a janky way to do this, testing this function quite a few times, it seems to work as intended.

    >>> countSeqBug(['a', 'b', 'c', 'c', 'c', 'd', 'e'])
    3
    >>> countSeqBug([])
    0
    """

    prev_item = []  # added variable declaration. Not necessarily needed, I personally like it declared here

    if len(alist) != 0:
        prev_item = alist[0]
        dup_ct = 1
        high_ct = 1

    else:
        high_ct = 0
        dup_ct = 0

    for i in range(1, len(alist)):
        if alist[i] == prev_item:
            dup_ct += 1

        else:
            prev_item = alist[i]

            if dup_ct > high_ct:
                high_ct = dup_ct
            dup_ct = 1

    return high_ct


def salesReportBug(salesli):
    """(list) --> None

    Prints report of sales totals for each day of week (salesli)
    and range of per-day sales. salesli is non-empty - 0 sales
    for any day are reported as 0.

    String formatting added a few spaces at the end. Add doctest.NORMALIZE_WHITESPACE to ignore whitespace so
    test can pass. Added <BLANKLINE> also so the test can pass successfully.

    >>> salesReportBug([40000, 45.67, 19000.0, 25000, 100000]) #doctest: +NORMALIZE_WHITESPACE
    Weekly Range: $45.67 - $100,000.00
    <BLANKLINE>
    Mon          Tue          Wed          Thu          Fri
    $40,000.00   $45.67       $19,000.00   $25,000.00   $100,000.00


    """

    # calculate and report low and high sales
    low, high = findRangeBug(salesli)
    # low = findRangeBug(salesli)
    print(f'Weekly Range: ${low:,.2f} - ${high:,.2f}\n')

    # print daily report header
    fw = 12
    print(f"{'Mon':<{fw}} {'Tue':<{fw}} {'Wed':<{fw}} {'Thu':<{fw}} {'Fri':<{fw}}")

    # report on sales per day from list data
    for sales in salesli:  # sort() from findRangeBug affects list in this function
        print(f'${float(sales):<{fw},.2f}', end='')

    return None


def findRangeBug(salesli):
    """(list) -> tuple

    Returns largest and smallest number in non-empty salesli.
    (Note that Python has built in funcs max and min
    to do this, but not using them here, so we can
    work with the list directly.)

    >>> findRangeBug([40000, 45.67, 19000.0, 25000, 100000])
    (45.67, 100000.0)
    """
    newSaleLi = salesli.copy()  # sort() returns none and affects alist in function above
    newSaleLi.sort()
    low = float(newSaleLi[0])  # changed variable to reflect changes to list name
    high = float(newSaleLi[-1])  # changed variable to reflect changes to list name

    return low, high


print(doctest.testmod())
