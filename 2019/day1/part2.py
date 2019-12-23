class Part2:

    @staticmethod
    def total_fuel_requirement(file: str):
        with open(file) as file:
            return sum([Part2.fuel_requirement(int(mass)) for mass in file])

    @staticmethod
    def fuel_requirement(mass: int):
        requirement = int(mass / 3) - 2
        if requirement > 0:
            return requirement + Part2.fuel_requirement(requirement)
        else:
            return 0


if __name__ == "__main__":
    result = Part2.total_fuel_requirement('input.txt')
    print("Result: " + str(result))  # 4914785
