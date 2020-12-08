import copy


def get_instructions():
    instructions = []
    with open('input.txt') as f:
        for line in f:
            instr, cnt_raw = line.split()
            cnt = int(cnt_raw)
            instructions.append((instr, cnt))

    return instructions


def run_program(instructions):
    visited = set()
    accumulator = 0
    instr_pointer = 0
    while True:
        if instr_pointer in visited:
            raise ValueError(accumulator)
        visited.add(instr_pointer)

        if instr_pointer >= len(instructions):
            return accumulator
        instr, cnt = instructions[instr_pointer]
        if instr == 'nop':
            instr_pointer += 1
        elif instr == 'acc':
            accumulator += cnt
            instr_pointer += 1
        elif instr == 'jmp':
            instr_pointer += cnt
        else:
            raise NotImplementedError


def task1():
    instructions = get_instructions()
    acc = 0
    try:
        acc = run_program(instructions)
    except ValueError as e:
        acc = e.args[0]
    return acc


def modify_instructions(instructions, offset):
    instr_mod = copy.deepcopy(instructions)
    for i, (instr, cnt) in enumerate(instr_mod[offset:], offset):
        if instr == 'nop':
            instr_mod[i] = ('jmp', cnt)
            return instr_mod
        elif instr == 'jmp':
            instr_mod[i] = ('nop', cnt)
            return instr_mod


def task2():
    instructions = get_instructions()
    i = 0
    while True:
        i += 1  # we can skip the first one as its task1
        instr_mod = modify_instructions(instructions, i)
        try:
            acc = run_program(instr_mod)
            return acc
        except ValueError:
            continue


def main():
    print(task1())
    print(task2())


if __name__ == "__main__":
    main()
