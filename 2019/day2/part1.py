def parse_data(file_name):
    with open(file_name, 'r') as file:
        program = list(file.read().split(","))
        return [int(position) for position in program]


def int_code(program):
    restored_program = restore(program)
    return compute(restored_program)


def restore(program):
    program[1] = 12
    program[2] = 2
    return program


def compute(program):
    for index in range(0, len(program), 4):
        opcode = program[index]
        if opcode == 99:
            return program

        first = program[index + 1]
        second = program[index + 2]
        store_at = program[index + 3]

        if opcode == 1:
            program[store_at] = program[first] + program[second]
        elif opcode == 2:
            program[store_at] = program[first] * program[second]

    return program


if __name__ == "__main__":
    data = parse_data('input.txt')
    result = int_code(data)
    print("Result: " + str(result[0]))  # 11590668
