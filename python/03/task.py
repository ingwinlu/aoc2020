TREE = '#'


def build_field():
    lines = open("input.txt").read().splitlines()
    return lines


def slope(step_down=1, step_right=3):
    field = build_field()
    tree_counter = 0
    sled_y = 0
    for line in field[0::step_down]:
        elem = line[sled_y]
        if elem == TREE:
            tree_counter += 1
        sled_y = (sled_y + step_right) % len(line)

    return tree_counter


def task1():
    return slope()


def task2():
    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    acc = 1
    for slope_candidate in slopes:
        acc *= slope(*slope_candidate)
    return acc


def main():
    print(task1())
    print(task2())


if __name__ == "__main__":
    main()
