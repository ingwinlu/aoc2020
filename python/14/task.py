def parse_mask(line):
    mask = line.split()[2]
    return mask


def parse_mem(line):
    mem_addr_raw, _, val_raw = line.split()
    val = int(val_raw)
    mem_add = int(mem_addr_raw[4:-1])
    return mem_add, val


def get_masked_value(mask, i):
    i_b = '{:036b}'.format(i)
    temp = ''
    for b, m in zip(i_b, mask):
        if m == 'X':
            temp += b
        else:
            temp += m
    return int(temp, 2)


def task1():
    programm = open('input.txt').readlines()
    state = {}
    for line in programm:
        if line.startswith('mask'):
            state["mask"] = parse_mask(line)
        elif line.startswith("mem"):
            memory = state.get('mem', dict())
            addr, unmasked_val = parse_mem(line)
            val = get_masked_value(state["mask"], unmasked_val)
            memory[addr] = val
            state['mem'] = memory

    return sum(state['mem'].values())


def build_addresses(temp):
    if len(temp) <= 0:
        return ['']
    c = temp[0]
    if c == "0" or c == "1":
        return [
            c + l
            for l in build_addresses(temp[1:])
        ]
    else:
        lists = build_addresses(temp[1:])
        return [
            "0" + l
            for l in lists
        ] + [
            "1" + l
            for l in lists

        ]


def mask_addresses(mask, addr):
    i_b = '{:036b}'.format(addr)
    temp = ''
    for b, m in zip(i_b, mask):
        if m == "0":
            temp += b
        elif m == "1":
            temp += "1"
        elif m == "X":
            temp += "X"

    return build_addresses(temp)


def task2():
    programm = open('input.txt').readlines()
    state = {}
    for line in programm:
        if line.startswith('mask'):
            state["mask"] = parse_mask(line)
        elif line.startswith("mem"):
            memory = state.get('mem', dict())
            addr, val = parse_mem(line)
            addr_list = mask_addresses(state["mask"], addr)
            for addr in addr_list:
                memory[addr] = val
            state['mem'] = memory
    return sum(state['mem'].values())


def main():
    print(task1())
    print(task2())


if __name__ == "__main__":
    main()
