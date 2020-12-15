INPUT = [9,19,1,6,0,5,4]


def finder(mem, abort):
    while True:
        # breakpoint()
        if len(mem) == abort:
            break
        last_spoken = mem[-1]
        try:
            idx = len(mem) - 1 - mem[:-1][::-1].index(last_spoken)
        except ValueError:
            mem.append(0)
            continue
        mem.append(
            len(mem) - idx
        )

    return mem[-1]


def memory_game(mem, end):
    d = {
        n: i
        for i, n in enumerate(mem[:-1])
    }
    last_spoken = mem[-1]
    for turn in range(len(mem), end):
        try:
            idx = d[last_spoken]
        except KeyError:
            spoken = 0
        else:
            spoken = turn - idx - 1
        d[last_spoken] = turn - 1
        last_spoken = spoken
    return last_spoken


def task1():
    return memory_game(INPUT.copy(), 2020)


def task2():
    return memory_game(INPUT.copy(), 30000000)


def main():
    print(task1())
    print(task2())

if __name__ == "__main__":
    main()
