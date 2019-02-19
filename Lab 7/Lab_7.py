def upperF(file):
    words = 0
    lines = 0
    char = 0
    with open(file) as fin:

        for i in fin:
            if len(i) > 2:
                words += 1
            char += len(i)
            lines += 1

            for x in i:
                if x == " ":
                    words += 1
        char = char - lines + 1
    print(words, lines, char)


upperF("2.txt")
