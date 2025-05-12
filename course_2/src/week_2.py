import heapq
from typing import Dict, List
from collections import deque


class GraphNode:
    def __init__(self, v: int, w: int) -> None:
        self.vertex = v
        self.weight = w

    def __repr__(self) -> str:
        return f"vertex: {self.vertex}, weight: {self.weight}"


def find_shortest_paths(graph: Dict[int, List[GraphNode]], source_vertex=1):
    Infinity = 1_000_000
    dist = [Infinity] * (len(graph) + 1)
    queue = deque(range(source_vertex, len(graph) + 1))
    dist[source_vertex] = 0
    # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

    while queue:
        u = queue[0]
        for vertex in queue:
            if dist[vertex] < dist[u]:
                u = vertex
        queue.remove(u)

        for v in graph[u]:
            # TODO: try heap later
            alt = dist[u] + v.weight
            if alt < dist[v.vertex]:
                dist[v.vertex] = alt

    return dist


if __name__ == "__main__":
    from pathlib import Path
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "txt_file", help="Text file contains 2 numbers seperated by new line", type=str
    )

    args = parser.parse_args()

    filepath: str = args.txt_file

    input_file = (Path.cwd() / filepath).resolve()

    graph = dict()

    with open(
        input_file,
        "r",
    ) as f:
        for line in f:
            temp = line.split()
            v, edges = int(temp[0]), temp[1:]
            graph[v] = []
            for e in edges:
                ve, w = map(int, e.split(","))
                graph[v].append(GraphNode(ve, w))

    shortest_paths = find_shortest_paths(graph)

    print(
        ",".join(
            map(
                lambda r: str(r),
                [
                    shortest_paths[i]
                    for i in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
                ],
            )
        )
    )
