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
    visited_points = {}
    x = 0
    y = 0
    steps = 0
    for vector in wire:
        direction = vector[0]
        length = int(vector[1:])

        x_step, y_step = step(direction)

        for _ in range(0, length):
            x += x_step
            y += y_step
            steps += 1

            if(x, y) not in visited_points:
                visited_points[(x, y)] = steps

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
    intersections = {}
    intersecting_points = set(wire1.keys()).intersection(set(wire2.keys()))
    for point in intersecting_points:
        intersections[point] = wire1[point] + wire2[point]
    return intersections


def calculate_min_distance(intersections):
    return min(intersections.values())


if __name__ == "__main__":
    wire1, wire2 = parse_data('input.txt')
    result = manhattan_distance(wire1, wire2)
    print("Result: " + str(result))  # 18542
