def parse_data(file_name):
    with open(file_name, 'r') as file:
        line = list(file.read().strip("\n"))
        return [int(position) for position in line]


def find_layer(image, height, width):
    masked = []
    while len(image) > 0:
        layer = take_layer(image, height, width)
        masked = mask(layer, masked)
    return masked


def take_layer(image, height, width):
    layer = []
    for _ in range(0, height):
        layer.append(image[:width])
        del image[:width]
    return layer


def mask(layer, masked):
    result = []
    for row_index in range(len(layer)):
        current_layer = layer[row_index]
        resulting_row = []
        for index in range(len(current_layer)):
            if len(masked) > 0 and masked[row_index][index] < 2:
                resulting_row.insert(index, masked[row_index][index])
            else:
                resulting_row.insert(index, current_layer[index])
        result.append(resulting_row)
    return result


if __name__ == "__main__":
    data = parse_data('input.txt')
    result = find_layer(data, 6, 25)
    print("Result:")  # CFCUG
    for row in result:
        print(str(row))
