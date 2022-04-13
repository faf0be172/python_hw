def head(filename: str, rows: int = 10):
    if rows < 0:
        raise TypeError("Rows number must be non-negative")

    with open(filename) as file:
        for _ in range(rows):
            print(file.readline(), end="")


def tail(filename: str, rows: int = 10):
    if rows < 0:
        raise TypeError("Rows number must be non-negative")

    with open(filename) as file:
        str_count = 0
        for _ in file:
            str_count += 1

    with open(filename) as file:
        file_iter = iter(file)
        for _ in range(str_count - rows):
            next(file_iter)
        for line in file_iter:
            print(line, end='')
        print()


def nl(filename: str, separator: str = "  ", tabs: int = 1):
    if tabs < 0:
        raise TypeError("Tabs number must be non-negative")

    with open(filename) as file:
        str_cnt = 0
        for line in file:
            if line.strip():
                print("\t" * tabs + str(str_cnt + 1) + separator + line.strip())
                str_cnt += 1


def wc(filename: str, rows: bool = True, words: bool = True, symbols: bool = True):
    with open(filename) as file:
        str_cnt = 0
        words_cnt = 0
        symbols_cnt = 0

        for line in file:
            str_cnt += 1
            words_cnt += len(line.strip().split())
            symbols_cnt += len(line)

        if symbols:
            print("Symbols: {}".format(symbols_cnt))
        if words:
            print("Words: {}".format(words_cnt))
        if rows:
            print("Rows: {}".format(str_cnt))


if __name__ == "__main__":
    head("text.txt", 3)
    tail("text.txt", 2)
    nl("text.txt", separator=". ")
    wc("text.txt")
