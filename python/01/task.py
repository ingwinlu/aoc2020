from itertools import product
from math import prod


def task(candidate_count: int = 2) -> int:
    ints = map(int, open("01/input.txt"))
    for candidate in product(ints, repeat=candidate_count):
        if sum(candidate) == 2020:
            return candidate, prod(candidate)
    raise ValueError("No suitable combo found")


def main():
    print(task(2))
    print(task(3))


if __name__ == "__main__":
    main()
