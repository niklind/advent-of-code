import typing


def int_code(file: str):
    with open(file, 'r') as file:
        raw = list(file.read().split(","))
        program = [int(position) for position in raw]
        restored_program = restore(program)
        return compute(restored_program)[0]


def restore(program: typing.List[int]):
    program[1] = 12
    program[2] = 2
    return program


def compute(program: typing.List[int]):
    pos = 0
    while len(program) > pos:
        opcode = program[pos]
        if opcode == 99:
            return program

        first = program[pos + 1]
        second = program[pos + 2]
        store_at = program[pos + 3]

        if opcode == 1:
            program[store_at] = program[first] + program[second]
        elif opcode == 2:
            program[store_at] = program[first] * program[second]

        pos += 4

    return program


if __name__ == "__main__":
    result = int_code('input.txt')
    print("Result: " + str(result))  # 11590668
