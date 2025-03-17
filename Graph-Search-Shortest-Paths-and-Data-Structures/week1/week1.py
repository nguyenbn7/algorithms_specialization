from typing import List
from collections import deque


def load_data(filename: str):
    with open(filename) as file:
        return file.readlines()


def find_scc(graph: List[List[int]], rev_graph: List[List[int]], len_graph: int):
    magic_order = DFS_loop(graph, len_graph)

    print("Done 1st pass")

    # replace node of by order of graph
    rev_labeled_graph = [[] for _ in range(len_graph)]
    for node in range(len_graph):
        k = magic_order[node]
        for edge in rev_graph[node]:
            rev_labeled_graph[k].append(magic_order[edge])

    print("Done label reverse")
    # Fix double count
    return DFS_loop_rev_labeled(rev_labeled_graph, len_graph)


def DFS_loop_rev_labeled(graph: List[List[int]], len_graph: int):
    # 2nd pass for rev_graph
    visited = [False] * len_graph
    # The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
    scc = [0] * len_graph

    for node in range(len_graph - 1, 0, -1):
        if not visited[node]:
            stack = deque([node])
            topo_stack = deque()
            while stack:
                v = stack[-1]
                visited[v] = True
                sink = True
                for e in graph[v][::-1]:
                    if not visited[e]:
                        sink = False
                        stack.append(e)
                        break
                # get back to leader vertex
                if sink:
                    topo_stack.append(stack.pop())
            scc[node] = len(topo_stack)
    return scc


def DFS_loop(graph: List[List[int]], len_graph: int):
    # 1st pass for original
    visited = [False] * len_graph
    order = [0] * len_graph
    t = 0

    for node in range(len_graph - 1, 0, -1):
        if not visited[node]:
            stack = deque([node])
            while stack:
                v = stack[-1]
                if not visited[v]:
                    visited[v] = True
                    for e in graph[v][::-1]:
                        if not visited[e]:
                            stack.append(e)
                # get back to original vertex
                if v == stack[-1]:
                    v = stack.pop()
                    # prevent sink makes order twice
                    if not order[v]:
                        t += 1
                        order[v] = t
    return order


if __name__ == "__main__":
    filename = "./final.txt"
    data = load_data(filename)
    data = [tuple(map(lambda x: int(x), l.split())) for l in data]
    len_graph = max(max(data)) + 1

    graph = [[] for _ in range(len_graph)]
    rev_graph = [[] for _ in range(len_graph)]

    for v, e in data:
        graph[v].append(e)
        rev_graph[e].append(v)

    scc = find_scc(graph, rev_graph, len_graph)
    scc.sort(reverse=True)
    print(scc[:5])
