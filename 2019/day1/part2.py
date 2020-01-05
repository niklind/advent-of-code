def parse_data(file_name):
    with open(file_name, 'r') as file:
        return [int(line) for line in file]


def total_fuel_requirement(masses):
    return sum([fuel_requirement(mass) for mass in masses])


def fuel_requirement(mass):
    requirement = int(mass / 3) - 2
    if requirement > 0:
        return requirement + fuel_requirement(requirement)
    else:
        return 0


if __name__ == "__main__":
    data = parse_data('input.txt')
    result = total_fuel_requirement(data)
    print("Result: " + str(result))  # 4914785
