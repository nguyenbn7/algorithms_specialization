# https://www.geeksforgeeks.org/introduction-and-implementation-of-kargers-algorithm-for-minimum-cut/
from typing import List
from random import choice


class Edge:
    def __init__(self, src: int, dest: int):
        self.src = src
        self.dest = dest


class Graph:
    def __init__(self, no_vertex: int, no_edge: int):
        self.no_vertex = no_vertex
        self.no_edge = no_edge

        self.edges: List[Edge] = []


# A class to represent a subset for union-find
class Subset:
    def __init__(self, parent: int, rank: int):
        self.parent = parent
        self.rank = rank


# A function that does union of two sets of x and y
# (uses union by rank)
def Union(subsets: List[Subset], x: int, y: int):
    x_root = find(subsets, x)
    y_root = find(subsets, y)

    # Attach smaller rank tree under root of high
    # rank tree (Union by Rank)
    if subsets[x_root].rank < subsets[y_root].rank:
        subsets[x_root].parent = y_root
    elif subsets[x_root].rank > subsets[y_root].rank:
        subsets[y_root].parent = x_root

    # If ranks are same, then make one as root and
    # increment its rank by one
    else:
        subsets[y_root].parent = x_root
        subsets[x_root].rank += 1


def find(subsets: List[Subset], i: int):
    # find root and make root as parent of i
    # (path compression)
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets, subsets[i].parent)

    return subsets[i].parent


def karger_min_cut(graph: Graph) -> int:
    V = graph.no_vertex
    E = graph.no_edge
    edges = graph.edges

    subsets = []

    for v in range(V + 1):
        subsets.append(Subset(v, 0))

    # Initially there are V vertices in
    # contracted graph
    vertices = V

    while vertices > 2:
        edge = choice(edges)
        # print(edge)

        subset1 = find(subsets, edge.src)
        subset2 = find(subsets, edge.dest)

        if subset1 == subset2:
            continue

        vertices -= 1
        Union(subsets, subset1, subset2)

    # Now we have two vertices (or subsets) left in
    # the contracted graph, so count the edges between
    # two components and return the count.
    cutedges = 0

    for i in range(E):
        subset1 = find(subsets, edges[i].src)
        subset2 = find(subsets, edges[i].dest)
        if subset1 != subset2:
            cutedges += 1

    return cutedges // 2


def min_cut(graph: Graph, iteration: int = 200):
    """
    Calculate Karger min cut for given graph
    """
    return min(karger_min_cut(graph) for _ in range(iteration))


if __name__ == "__main__":
    from pathlib import Path
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "txt_file",
        help="Text file contains numbers seperated by new line and space",
        type=str,
    )

    args = parser.parse_args()

    filepath: str = args.txt_file

    input_file = (Path.cwd() / filepath).resolve()

    graph = Graph(0, 0)

    with open(
        input_file,
        "r",
    ) as f:
        lines = f.readlines()
        for line in lines:
            temp = list(map(int, line.split()))

            graph.no_vertex += 1
            graph.no_edge += len(temp[1:])

            for dest in temp[1:]:
                graph.edges.append(Edge(temp[0], dest))

    print(min_cut(graph))
