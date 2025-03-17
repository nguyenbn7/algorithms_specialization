from typing import Dict, List
from random import choice
from copy import deepcopy


def min_cut(graph: Dict[int, List[int]], iteration: int = 200):
    return min(karger_min_cut(graph) for _ in range(iteration))


# https://www.geeksforgeeks.org/kargers-algorithm-for-minimum-cut-set-1-introduction-and-implementation/
def karger_min_cut(graph: Dict[int, List[int]]) -> int:
    graph_copy = deepcopy(graph)
    while len(graph_copy) > 2:
        base_vertex = choice(list(graph_copy.keys()))
        merge_vertex = choice(graph_copy[base_vertex])

        if base_vertex == merge_vertex:
            continue

        __contract(graph_copy, base_vertex, merge_vertex)
    # They are symmetric so use both case is ok
    return len(graph_copy[next(iter(graph_copy))])


def __contract(graph: Dict[int, List[int]], base_vertex: int, merge_vertex: int):
    # contract between base and vertex wanted to merge
    graph[base_vertex].extend(
        list(filter(lambda vertex: vertex != base_vertex, graph[merge_vertex]))
    )
    # Remove self loop
    graph[base_vertex] = list(
        filter(lambda vertex: vertex != merge_vertex, graph[base_vertex])
    )

    for vertex, vertices in graph.items():
        if vertex == base_vertex or vertex == merge_vertex:
            continue

        while True:
            if merge_vertex not in vertices:
                break
            vertices[vertices.index(merge_vertex)] = base_vertex

    # remove vertex after merge
    del graph[merge_vertex]
