def parse_data(file_name):
    with open(file_name, 'r') as file:
        line = list(file.read().strip("\n"))
        return [int(position) for position in line]


def find_layer(image, height, width):
    min_zeros = 99
    min_layer = []
    while len(image) > 0:
        layer = take_layer(image, height, width)
        flattened_layer = flatten(layer)
        zeros = len(list(filter(lambda x: x == 0, flattened_layer)))
        print(zeros)
        if zeros < min_zeros:
            min_zeros = zeros
            min_layer = layer

    flattened_layer = flatten(min_layer)
    ones = len(list(filter(lambda x: x == 1, flattened_layer)))
    twos = len(list(filter(lambda x: x == 2, flattened_layer)))

    return ones * twos


def take_layer(image, height, width):
    layer = []
    for _ in range(0, height):
        layer.append(image[:width])
        del image[:width]
    return layer


def flatten(values):
    return [flattened for value in values for flattened in value]


if __name__ == "__main__":
    data = parse_data('input.txt')
    result = find_layer(data, 6, 25)
    print("Result: " + str(result))  # 46014
