def parse_data(file_name):
    with open(file_name, 'r') as file:
        wire1 = list(file.readline().split(","))
        wire2 = list(file.readline().split(","))
        return wire1, wire2


def manhattan_distance(wire1, wire2):
    wire1_path = calculate_path(wire1)
    wire2_path = calculate_path(wire2)
    intersections = find_intersections(wire1_path, wire2_path)
    return calculate_min_distance(intersections)


def calculate_path(wire):
    visited_points = set()
    x = 0
    y = 0
    for vector in wire:
        direction = vector[0]
        length = int(vector[1:])

        x_step, y_step = step(direction)

        for _ in range(0, length):
            x += x_step
            y += y_step
            visited_points.add((x, y))

    return visited_points


def step(direction):
    x_diff = 0
    y_diff = 0

    if direction == 'L':
        x_diff = -1
    elif direction == 'R':
        x_diff = 1
    elif direction == 'U':
        y_diff = 1
    elif direction == 'D':
        y_diff = -1

    return x_diff, y_diff


def find_intersections(wire1, wire2):
    return wire1.intersection(wire2)


def calculate_min_distance(intersections):
    distances = [calculate_distance(intersection) for intersection in intersections]
    return min(distances)


def calculate_distance(intersection):
    return abs(intersection[0]) + abs(intersection[1])


if __name__ == "__main__":
    wire1, wire2 = parse_data('input.txt')
    result = manhattan_distance(wire1, wire2)
    print("Result: " + str(result))  # 221
