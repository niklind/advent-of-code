def parse_data(file_name):
    with open(file_name, 'r') as file:
        interval = file.readline().split("-")
        return int(interval[0]), int(interval[1])


def find_valid_passwords(low, high):
    valid_passwords = 0
    for password in range(low, high):
        if validate_password(password):
            valid_passwords += 1
    return valid_passwords


def validate_password(password):

    numbers = [int(x) for x in str(password)]
    if len(numbers) != 6:
        return False

    previous = 0
    has_double = False

    for number in numbers:
        if number < previous:
            return False
        elif number == previous and not has_double:
            has_double = True
        previous = number

    return has_double


if __name__ == "__main__":
    low, high = parse_data('input.txt')
    result = find_valid_passwords(low, high)
    print("Result: " + str(result))  # 466
