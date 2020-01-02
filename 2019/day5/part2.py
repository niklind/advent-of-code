import typing


def parse_data(file: str):
    with open(file, 'r') as file:
        program = list(file.read().split(","))
        return [int(position) for position in program]


def int_code(program: typing.List[int], input_code: int):
    index = 0
    diagnostic_code = 0
    while index < len(program)-1:
        modes, opcode = read_instructions(index, program)

        offset_1 = value(modes[0], index + 1, program)
        offset_2 = value(modes[1], index + 2, program)
        offset_3 = value(modes[2], index + 3, program)

        if opcode == 1:
            program[offset_3] = program[offset_1] + program[offset_2]
            index += 4
        elif opcode == 2:
            program[offset_3] = program[offset_1] * program[offset_2]
            index += 4
        elif opcode == 3:
            program[offset_1] = input_code
            index += 2
        elif opcode == 4:
            diagnostic_code = program[offset_1]
            index += 2
        elif opcode == 5:
            if program[offset_1] != 0:
                index = program[offset_2]
            else:
                index += 3
        elif opcode == 6:
            if program[offset_1] == 0:
                index = program[offset_2]
            else:
                index += 3
        elif opcode == 7:
            if program[offset_1] < program[offset_2]:
                program[offset_3] = 1
            else:
                program[offset_3] = 0
            index += 4
        elif opcode == 8:
            if program[offset_1] == program[offset_2]:
                program[offset_3] = 1
            else:
                program[offset_3] = 0
            index += 4
        elif opcode == 99:
            return diagnostic_code

    return diagnostic_code


def read_instructions(index, program):
    instruction = f"{program[index]:05d}"
    opcode = int(instruction[3] + instruction[4])
    modes = [int(mode) for mode in reversed(instruction[:3])]
    return modes, opcode


def value(mode, number, program):
    if mode == 1:
        return number
    elif mode == 0:
        return program[number] if number < len(program) else 0


if __name__ == "__main__":
    data = parse_data('input.txt')
    result = int_code(data, 5)
    print("Result: " + str(result))  # 2808771
