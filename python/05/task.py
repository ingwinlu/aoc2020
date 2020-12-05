from itertools import tee
from typing import List


def bsp_naive(myrange: List[int], bools: List[bool]):
    split = int(len(myrange) / 2)
    if bools[0]:
        newrange = myrange[split:]
    else:
        newrange = myrange[:split]
    if len(newrange) == 1:
        return newrange[0]
    return bsp_naive(newrange, bools[1:])


TRUE_MAP = ['B', 'R']
ROW_COLUMN_INDEX = 7


def bp_to_id(bp):
    binarymapping = [
        True if char in TRUE_MAP else False
        for char in list(bp)
    ]

    rows = binarymapping[:ROW_COLUMN_INDEX]
    columns = binarymapping[ROW_COLUMN_INDEX:]

    row = bsp_naive(list(range(128)), rows)
    column = bsp_naive(list(range(8)), columns)

    return row * 8 + column


def task1():
    boardingpasses_combined = open('input.txt').read().splitlines()

    ids = map(bp_to_id, boardingpasses_combined)
    max_id = max(ids)
    return max_id


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def task2():
    boardingpasses_combined = open('input.txt').read().splitlines()
    ids = sorted(list(map(bp_to_id, boardingpasses_combined)))
    for x, y in pairwise(ids):
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
