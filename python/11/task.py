from copy import deepcopy

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'


def get_area():
    # [y][x] from top left
    return list(map(
        list,
        open('input.txt').read().splitlines()
    ))


def adjacent_occupied(area, y, x):
    occupied = 0
    for c_y in range(y-1, y+2):
        if c_y < 0:
            continue
        if c_y >= len(area):
            continue
        for c_x in range(x-1, x+2):
            if c_x < 0:
                continue
            if c_x >= len(area[y]):
                continue
            if c_y == y and c_x == x:
                continue
            if area[c_y][c_x] == OCCUPIED:
                occupied += 1
    return occupied


def occupy(area):
    new_area = deepcopy(area)
    for y in range(len(area)):
        for x in range(len(area[y])):
            current = area[y][x]
            occupied = adjacent_occupied(area, y, x)
            if current == EMPTY:
                if occupied == 0:
                    new_area[y][x] = OCCUPIED
            elif current == OCCUPIED:
                if occupied >= 4:
                    new_area[y][x] = EMPTY
            else:
                continue
    return new_area


def count_occupied(area):
    cnt = 0
    for y in area:
        for x in y:
            if x == OCCUPIED:
                cnt += 1
    return cnt


def area_eqality(area1, area2):
    for lines in zip(area1, area2):
        for a, b in zip(*lines):
            if a != b:
                return False
    return True


def task1():
    area = get_area()
    while True:
        area_new = occupy(area)
        if area_eqality(area, area_new):
            break
        area = area_new

    return count_occupied(area)


def find_occupied(area, candidates):
    for y, x in candidates:
        if area[y][x] == FLOOR:
            continue
        elif area[y][x] == EMPTY:
            return False
        else:
            return True


def adjacent_occupied2(area, y, x):
    occupied = 0
    # down

    if find_occupied(area, (
                (c_y, x)
                for c_y in range(y+1, len(area))
            )):
        occupied += 1

    # up
    if find_occupied(area, (
                (c_y, x)
                for c_y in range(y-1, -1, -1)
            )):
        occupied += 1

    # right
    if find_occupied(area, (
                (y, c_x)
                for c_x in range(x+1, len(area[y]))
            )):
        occupied += 1

    # left
    if find_occupied(area, (
                (y, c_x)
                for c_x in range(x-1, -1, -1)
            )):
        occupied += 1

    # down right
    x_len = len(area[0])
    if find_occupied(area, zip(
                            range(y+1, len(area)),
                            range(x+1, x_len)
                            )):
        occupied += 1

    # down left
    if find_occupied(area, zip(
                            range(y+1, len(area)),
                            range(x-1, -1, -1)
                            )):
        occupied += 1

    # up right
    if find_occupied(area, zip(
                            range(y-1, -1, -1),
                            range(x+1, x_len)
                            )):
        occupied += 1

    # up left
    if find_occupied(area, zip(
                            range(y-1, -1, -1),
                            range(x-1, -1, -1)
                            )):
        occupied += 1

    return occupied


def occupy2(area):
    new_area = deepcopy(area)
    for y in range(len(area)):
        for x in range(len(area[y])):
            current = area[y][x]
            if current == EMPTY:
                occupied = adjacent_occupied2(area, y, x)
                if occupied == 0:
                    new_area[y][x] = OCCUPIED
            elif current == OCCUPIED:
                occupied = adjacent_occupied2(area, y, x)
                if occupied >= 5:
                    new_area[y][x] = EMPTY
            else:
                continue
    return new_area


def task2():
    area = get_area()
    while True:
        area_new = occupy2(area)
        if area_eqality(area, area_new):
            break
        area = area_new
    return count_occupied(area)


def main():
    print(task1())
    print(task2())


if __name__ == "__main__":
    main()
