ROW_COLUMN_INDEX = 7


def read_to_bin():
    return (
        open('input.txt').read()
                         .replace("B", "1")
                         .replace("F", "0")
                         .replace("R", "1")
                         .replace("L", "0")
                         .splitlines()
    )


def bp_to_id(bp):
    row = int(
        bp[:ROW_COLUMN_INDEX], 2
    )
    column = int(
        bp[ROW_COLUMN_INDEX:], 2
    )
    return row * 8 + column


def task1():
    bp_bins = read_to_bin()
    ids = map(bp_to_id, bp_bins)
    max_id = max(ids)
    return max_id


def task2():
    bp_bins = read_to_bin()
    ids = sorted(list(map(bp_to_id, bp_bins)))
    for i in range(0, len(ids)-1):
        x = ids[i]
        y = ids[i+1]
        expected = x + 1
        if expected == y:
            continue
        return expected
    raise ValueError


def main():
    print(task1())
    print(task2())


if __name__ == "__main__":
    main()
