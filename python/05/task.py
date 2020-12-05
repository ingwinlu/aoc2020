TRUE_MAP = ['B', 'R']
ROW_COLUMN_INDEX = 7


def bsp(bp, one='B', zero='F'):
    binarymapping = bp.replace(one, "1").replace(zero, "0")
    return int(binarymapping, 2)


def bp_to_id(bp):
    row = bsp(bp[:ROW_COLUMN_INDEX])
    column = bsp(bp[ROW_COLUMN_INDEX:], 'R', 'L')
    return row * 8 + column


def task1():
    boardingpasses_combined = open('input.txt').read().splitlines()
    ids = map(bp_to_id, boardingpasses_combined)
    max_id = max(ids)
    return max_id


def task2():
    boardingpasses_combined = open('input.txt').read().splitlines()
    ids = sorted(list(map(bp_to_id, boardingpasses_combined)))
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
