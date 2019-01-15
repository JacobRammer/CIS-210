import turtle



def is_even(n):
    """
        # TODO
    """

    print("in function is_even")

    return (n % 2) == 0


# result = is_even(3)
# print(result)
# print(dir())

# print(is_even(2))
# result = is_even(3)


def welcome():
    """
        # TODO
    """

    print("Good afternoon, CIS 210!")
    return None


# check = welcome()
# check
# print(check)
# print(welcome())


def est_tax(income, exemptions):
    """
        # TODO
            # page 5
    """

    # Set values needed to generate estimate
    STD_EXEMPT = 4150
    STD_DEDUCT = 6500
    TAX_RATE = .20

    # Calculate federal rax by adjusting
    # reported income and applying tax rate
    taxable_income = taxable(income, exemptions, STD_EXEMPT, STD_DEDUCT)
    estimated_tax = taxable_income * TAX_RATE

    print("Estimated tax is: ", estimated_tax)

    return None


def taxable(income, exemptions, STD_EXEMPT, STD_DEDUCT):
    """
    # TODO
        # page 5
    :param income:
    :param exemptions:
    :param STD_EXEMPT:
    :param STD_DEDUCT:
    :return:
    """

    taxable_income = income - STD_DEDUCT
    exempt_adjust = STD_EXEMPT * exemptions
    taxable_income = taxable_income - exempt_adjust

    print(taxable_income)
    return None

