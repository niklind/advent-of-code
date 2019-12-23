class Part1:

    @staticmethod
    def total_fuel_requirement(file: str):
        with open(file) as file:
            return sum([Part1.fuel_requirement(int(mass)) for mass in file])

    @staticmethod
    def fuel_requirement(mass: int):
        return int(mass / 3) - 2


if __name__ == "__main__":
    result = Part1.total_fuel_requirement('input.txt')
    print("Result: " + str(result))  # 3278434
