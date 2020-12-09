import itertools

BLOCKSIZE = 25


def read_to_num_list():
    return list(map(
        int,
        open('input.txt').read().split()
    ))


def find_invalid_number(numbers):
    for i in range(len(numbers)):
        found = False
        preamble = numbers[i:i+BLOCKSIZE]
        candidate = numbers[i+BLOCKSIZE]
        for a, b in itertools.combinations(preamble, 2):
            if a + b == candidate:
                found = True
                break
        if not found:
            return candidate
    raise ValueError


def task1():
    numbers = read_to_num_list()
    invalid = find_invalid_number(numbers)
    return invalid


def task2():
    numbers = read_to_num_list()
    invalid = find_invalid_number(numbers)
    start = 0
    end = 1
    while True:
        candidates = numbers[start:end]
        candidates_sum = sum(candidates)
        if candidates_sum == invalid:
            return min(candidates) + max(candidates)
        elif candidates_sum > invalid:
            start += 1
            end = start + 1
        end += 1


def main():
    print(task1())
    print(task2())


if __name__ == "__main__":
    main()
