def parse_data(file: str):
    with open(file, 'r') as file:
        interval = file.readline().split("-")
        return int(interval[0]), int(interval[1])


def find_valid_passwords(low, high):
    valid_passwords = []
    for password in range(low, high + 1):
        if validate_password(password):
            valid_passwords.append(password)
    return len(valid_passwords)


def validate_password(password):
    numbers = [int(x) for x in str(password)]
    previous = 0
    group = {}

    for number in numbers:
        if number < previous:
            return False
        elif number == previous:
            group[number] = group.get(number, 1) + 1
        previous = number

    has_groups_of_two = list(group.values()).count(2) > 0
    return has_groups_of_two


if __name__ == "__main__":
    low, high = parse_data('input.txt')
    result = find_valid_passwords(low, high)
    print("Result: " + str(result))  # 292
