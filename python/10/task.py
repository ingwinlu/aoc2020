def get_adapters():
    return list(map(
        int,
        open('input.txt').readlines()
    ))


def task1():
    adapters = get_adapters()
    adapters.sort()
    adapters[0:0] = [0]
    adapters.append(adapters[-1] + 3)

    diffs = map(
        lambda tmpl: tmpl[1]-tmpl[0],
        zip(adapters, adapters[1:])
    )

    diff_counter = {}
    for d in diffs:
        cnter = diff_counter.get(d, 0)
        cnter += 1
        diff_counter[d] = cnter

    return diff_counter[1] * diff_counter[3]


def ways(adapters, i, cache):
    if i in cache:
        return cache[i]

    if i >= len(adapters) - 1:
        return 1

    res = 0
    for j in range(i+1, i+4):
        if j < len(adapters) and adapters[j] - adapters[i] <= 3:
            res += ways(adapters, j, cache)
    cache[i] = res
    return res


def task2():
    adapters = get_adapters()
    adapters.sort()
    adapters[0:0] = [0]
    adapters.append(adapters[-1] + 3)

    return ways(adapters, 0, {})


def main():
    print(task1())
    print(task2())


if __name__ == "__main__":
    main()
