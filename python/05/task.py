TRUE_MAP = ['B', 'R']
ROW_COLUMN_INDEX = 7


def bsp(bp):
    binarymapping = ''.join([
        "1" if char in TRUE_MAP else "0"
        for char in list(bp)
    ])
    return int(binarymapping, 2)


def bp_to_id(bp):
    row = bsp(bp[:ROW_COLUMN_INDEX])
    column = bsp(bp[ROW_COLUMN_INDEX:])
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
