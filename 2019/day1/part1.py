def total_fuel_requirement(file: str):
    with open(file, 'r') as file:
        masses = [int(line) for line in file]
        return sum([fuel_requirement(mass) for mass in masses])


def fuel_requirement(mass: int):
    return int(mass / 3) - 2


if __name__ == "__main__":
    result = total_fuel_requirement('input.txt')
    print("Result: " + str(result))  # 3278434
