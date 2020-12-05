import re
from typing import Tuple

PWD_RE = re.compile(r"^(\d+)-(\d+) (\w): (\w+)$")


def parse(line: str) -> Tuple[int, int, str, str]:
    match = PWD_RE.fullmatch(line)
    minimum_str, maximum_str, letter, pwd = match.groups()
    minimum = int(minimum_str)
    maximum = int(maximum_str)
    return minimum, maximum, letter, pwd


def check_valid_pwd_1(line: str) -> bool:
    minimum, maximum, letter, pwd = parse(line)
    counter = 0
    for cur in pwd:
        if cur == letter:
            counter += 1

    if (minimum > counter) or (maximum < counter):
        return False
    return True


def check_valid_pwd_2(line: str) -> bool:
    fst, snd, letter, pwd = parse(line)
    fst -= 1
    snd -= 1

    return (pwd[fst] == letter) != (pwd[snd] == letter)


def task(validator):
    lines = open("input.txt").read().splitlines()
    valid_pwds = list(
        filter(validator, lines)
    )
    return len(valid_pwds)


def main():
    print(task(check_valid_pwd_1))
    print(task(check_valid_pwd_2))


if __name__ == "__main__":
    main()
