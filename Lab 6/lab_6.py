def greeting(f, s):
    print("Caling",f.__name__ )
    f(s)

    return None


def ciao(s):
    print("Chia, " + s + ".")

    return None


def hello(s):
    print("Hello, " + s + ".")

    return None


# greeting(hello, "World")
# greeting(ciao, "earth")

days = ["Mo", "Tu", "We", "Tu"]
temps = [55, 23, 42, 44]


def createTempD(daysL=days, tempsL = temps):

    dd = {}

    a = 0
    for i, t in zip(days, temps):
        dd[i] = t
        a += 1

    print(dd["We"])
    dd["Fr"] = 32
    dd["Sa"] = 60
    dd["Su"] =10

    temp_list = []
    for i in dd.values():
        temp_list.append(i)

    temp_list.sort()

    print(temp_list)

    return dd


print(createTempD())


def my_in(li, i):

    if i in li:
        return True
    else:
        return False


derp = ["a", "b"]

print(my_in(derp, "a"))
