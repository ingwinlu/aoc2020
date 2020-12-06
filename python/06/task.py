def task1():
    groups = open('input.txt').read().split('\n\n')
    acc = 0
    for group in groups:
        shared = set()
        for person in group.splitlines():
            s = set(person)
            shared = shared | s
        acc += len(shared)
    return acc


def task2():
    groups = open('input.txt').read().split('\n\n')
    acc = 0
    for group in groups:
        joined = set.intersection(
            *map(set, group.splitlines())
        )
        acc += len(joined)
    return acc
    pass


def main():
    print(task1())
    print(task2())


if __name__ == "__main__":
    main()
