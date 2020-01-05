import itertools


def parse_data(file_name):
    with open(file_name, 'r') as file:
        program = list(file.read().split(","))
        return [int(position) for position in program]


def amplifier_combinations(program):
    phases = [5, 6, 7, 8, 9]
    maximum_signal = 0
    for phase_setting in itertools.permutations(phases):
        maximum_signal = max(maximum_signal, amplifier(program.copy(), phase_setting))
    return maximum_signal


def amplifier(program, phase_settings):
    output = 0
    program_states = {}
    completed = False
    while not completed:
        for index in range(0, 5):
            input_program, input_position, input_codes = program_states.get(index, (program.copy(), 0, [phase_settings[index]]))
            input_codes.append(output)
            output_program, output_position, output = int_code(input_program, input_position, input_codes)
            program_states[index] = (output_program, output_position, input_codes)
            if output_position == 0:
                completed = True

    return output


def int_code(program, index, input_codes):
    diagnostic_code = input_codes[0]
    while index < len(program) - 1:
        modes, opcode = read_instructions(index, program)

        if opcode == 99:
            return program, 0, diagnostic_code

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
            program[offset_1] = input_codes.pop(0)
            index += 2
        elif opcode == 4:
            diagnostic_code = program[offset_1]
            index += 2
            return program, index, diagnostic_code
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

    return program, index, diagnostic_code


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
    result = amplifier_combinations(data)
    print("Result: " + str(result))  # 19581200
