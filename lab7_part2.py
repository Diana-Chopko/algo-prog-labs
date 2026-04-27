def get_weight(edge):
    """
    Used as a key function for sorting the edges.
    :param edge: line between wells.
    :return: the weight of edge.
    """
    return edge[2]


def find_parent(parent, node):
    """
    Finds the root of the set to which the given node belongs.
    Used to check if two nodes are already connected.
    :param parent: dictionary tracking system.
    :param node: one single well.
    :return: curr_node.
    """
    curr_node = node
    while parent[curr_node] != curr_node:
        curr_node = parent[curr_node]
    return curr_node


def union_sets(parent, node1, node2):
    """
    Merges two different groups of nodes into one by connecting
    their roots.
    :param parent: dictionary tracking system.
    :param node1: the well number 1.
    :param node2: the well number 2.
    """
    root1 = find_parent(parent, node1)
    root2 = find_parent(parent, node2)
    if root1 != root2:
        parent[root1] = root2


def calculate_min_cable(edges):
    """
    Calculates the minimum total cable length required to connect
    all peaks (wells) using Kruskal's algorithm.
    :param edges: line between wells.
    :return: -1 or min_len of the graph.
    """
    peaks = []
    for a, b, weight in edges:
        if a not in peaks:
            peaks.append(a)
        if b not in peaks:
            peaks.append(b)

    parent = {}
    for peak in peaks:
        parent[peak] = peak

    sorted_edges = sorted(edges, key=get_weight)
    min_len = 0
    edges_count = 0

    for a, b, weight in sorted_edges:
        root_a = find_parent(parent, a)
        root_b = find_parent(parent, b)

        if root_a != root_b:
            union_sets(parent, root_a, root_b)
            min_len += weight
            edges_count += 1

    result = -1
    if len(peaks) == 0:
        result = 0
    elif edges_count == len(peaks) - 1:
        result = min_len

    return result


def process_file_data(file_path):
    """
    Reads network data from a CSV file and triggers the calculation.
    :param file_path: the path to the file.
    :return: minimum cable length or an error message.
    """
    edges = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    a = parts[0].strip()
                    b = parts[1].strip()
                    dist = int(parts[2].strip())
                    edges.append((a, b, dist))
        result = calculate_min_cable(edges)
    except FileNotFoundError:
        result = "File not found"

    return result
