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
    return count_orbits(nodes)


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


def count_orbits(nodes):
    root = find_root(nodes)
    return count(root, 0)


def find_root(nodes):
    for key, value in nodes.items():
        if not value.parent:
            return value


def count(node, depth):
    orbits = depth
    if not node.children:
        return depth

    for child in node.children:
        orbits += count(child, depth + 1)
    return orbits


if __name__ == "__main__":
    data = parse_data('input.txt')
    result = find_orbits(data)
    print("Result: " + str(result))  # 453028
