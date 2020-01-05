class Node(object):
    """Generic tree node."""
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def __repr__(self):
        return "Node(" + self.name + ")"

    def add_parent(self, node):
        assert isinstance(node, Node)
        self.parent = node

    def add_child(self, node):
        assert isinstance(node, Node)
        self.children.append(node)


def parse_data(file_name):
    with open(file_name, 'r') as file:
        return [line.strip("\n") for line in file]


def find_orbits(relations):
    nodes = {}
    for relation in relations:
        child, parent = parse_relation(relation)
        add_orbit(child, parent, nodes)
    return count_orbital_transfers(nodes['YOU'], nodes['SAN'])


def parse_relation(line):
    relation = line.split(")")
    return relation[1], relation[0]


def add_orbit(current, parent, nodes):
    current_node = nodes.get(current, Node(current))
    parent_node = nodes.get(parent, Node(parent))

    current_node.add_parent(parent_node)
    parent_node.add_child(current_node)

    nodes[current] = current_node
    nodes[parent] = parent_node


def count_orbital_transfers(origin, destination):
    steps = 0
    current = origin.parent
    while True:
        depth = has_child(current, destination, 0)
        if depth > -1:
            return steps + depth
        current = current.parent
        steps += 1


def has_child(current, destination, depth):
    if destination in current.children:
        return depth

    depth += 1
    for child in current.children:
        temp = has_child(child, destination, depth)
        if temp > -1:
            return temp

    return -1


if __name__ == "__main__":
    data = parse_data('input.txt')
    result = find_orbits(data)
    print("Result: " + str(result))  # 562
