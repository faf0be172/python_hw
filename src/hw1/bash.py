def head(filename, rows=10):
    if type(filename) != str:
        raise TypeError("Invalid filename")
    if type(rows) != int or rows <= 0:
        raise TypeError("Invalid rows number")

    with open(filename, "r") as file:
        print(*[s.strip() for s in file.readlines()[:rows]], sep="\n")


def tail(filename, rows=10):
    if type(filename) != str:
        raise TypeError("Invalid filename")
    if type(rows) != int or rows <= 0:
        raise TypeError("Invalid rows number")

    with open(filename, "r") as file:
        print(*[s.strip() for s in file.readlines()[-rows:]], sep="\n")


def nl(filename, separator="  ", tabs=1):
    if type(filename) != str:
        raise TypeError("Invalid filename")
    if type(separator) != str:
        raise TypeError("Invalid separator type")
    if type(tabs) != int or tabs < 0:
        raise TypeError("Invalid tabs number")

    with open(filename, "r") as file:
        rows = file.readlines()
        print(
            *["\t" * tabs + str(number + 1) + separator + row.strip() for (number, row) in zip(range(len(rows)), rows)],
            sep="\n"
        )


def wc(filename, rows=True, words=True, symbols=True):
    if type(filename) != str:
        raise TypeError("Invalid filename")
    if type(rows) != bool:
        raise TypeError("Invalid rows flag type")
    if type(words) != bool:
        raise TypeError("Invalid words flag type")
    if type(symbols) != bool:
        raise TypeError("Invalid symbols flag type")

    with open(filename, "r") as file:
        rows_number = len(file.readlines())
        assert rows_number >= 0

        file.seek(0, 0)
        text = file.read()
        words_number = len(text.replace("\n", " ").split(" "))
        assert words_number >= 0

        symbols_number = len(text)
        assert symbols_number >= 0

        if symbols:
            print("Symbols: {}".format(symbols_number))
        if words:
            print("Words: {}".format(words_number))
        if rows:
            print("Rows: {}".format(rows_number))


if __name__ == "__main__":
    head("text.txt", 3)
    print()
    tail("text.txt", 3)
    print()
    nl("text.txt", separator=". ")
    print()
    wc("text.txt")
