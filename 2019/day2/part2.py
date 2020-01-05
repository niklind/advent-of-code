def parse_data(file_name):
    with open(file_name, 'r') as file:
        program = list(file.read().split(","))
        return [int(position) for position in program]


def int_code(program):
    for noun in range(0, 99):
        for verb in range(0, 99):
            restored_program = restore(noun, verb, program.copy())
            computed = compute(restored_program)
            if computed[0] == 19690720:
                return computed


def restore(noun, verb, program):
    program[1] = noun
    program[2] = verb
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
    print("Result: " + str(result[1]) + str(result[2]))  # 2254
