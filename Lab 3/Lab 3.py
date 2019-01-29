from math import pi



def pizza_calculator(diameter, cost):
    """

    :param diameter:
    :param cost:
    :return:
    """

    r = diameter / 2
    area = pi * r ** 2
    cost_per_inch = round(cost / area, 3)

    return cost_per_inch


pizza1 = pizza_calculator(20, 31.42)


# print(pizza1)


def circle_area(radius):
    """


    :param radius:
    :return:
    """
    area = pi * radius

    return area


def main():
    print("Pizza 1: ", pizza_calculator(14, 18))
    print("Pizza 2: ", pizza_calculator(14, 20.25))
    print("Pizza 3: ", pizza_calculator(20, 27))


main()
