import typing


def int_code(file: str):
    with open(file, 'r') as file:
        raw = list(file.read().split(","))
        program = [int(position) for position in raw]
        for noun in range(0, 99):
            for verb in range(0, 99):
                restored_program = restore(noun, verb, program.copy())
                computed = compute(restored_program)
                if computed[0] == 19690720:
                    return computed


def restore(noun: int, verb: int, program: typing.List[int]):
    program[1] = noun
    program[2] = verb
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
    print("Result: " + str(result[1]) + str(result[2]))  # 2254
