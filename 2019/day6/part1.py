def parse_data(file: str):
    with open(file, 'r') as file:
        return [line.strip("\n") for line in file]

# TODO change to tree
def find_orbits(relations):
    orbits = {}
    for relation in relations:
        child, parent = parse_relation(relation)
        orbit(child, parent, orbits)
    all_orbits = flatten(orbits.values())
    return len(all_orbits)


def flatten(values):
    return [flattened for value in values for flattened in value]


def orbit(current, parent, orbits):
    parent_orbits = orbits.get(parent, {})
    current_orbits = {parent}.union(parent_orbits)
    orbits[current] = current_orbits
    for key, value in orbits.items():
        if current in value:
            orbits[key] = value.union(current_orbits)


def parse_relation(line):
    relation = line.split(")")
    return relation[1], relation[0]


if __name__ == "__main__":
    data = parse_data('input.txt')
    result = find_orbits(data)
    print("Result: " + str(result))  # 453028
