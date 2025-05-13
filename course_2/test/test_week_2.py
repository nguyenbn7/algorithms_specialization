from pathlib import Path

import pytest
import test as _

from src.week_2 import find_shortest_paths, GraphNode

current_path = Path(__file__).parent.resolve()

input_test_path = current_path / "input/week_2"
input_test_filenames = [f.name for f in input_test_path.glob("*.txt")]

output_test_path = current_path / "output/week_2"
output_test_filenames = [f.name for f in output_test_path.glob("*.txt")]


def get_graph(filename: str):
    graph = {}

    with open(
        input_test_path / filename,
        "r",
    ) as f:
        for line in f:
            temp = line.split()
            v, edges = int(temp[0]), temp[1:]
            graph[v] = []
            for e in edges:
                ve, w = map(int, e.split(","))
                graph[v].append(GraphNode(ve, w))

        return graph


def get_expected_test_result(filename):
    with open(
        output_test_path / filename,
        "r",
    ) as f:
        return list(map(int, f.readline().split(",")))


@pytest.mark.parametrize(
    "input_filename,output_filename",
    [*zip(input_test_filenames, output_test_filenames)],
)
def test_graph_shortest_paths(input_filename, output_filename):
    expected = get_expected_test_result(output_filename)

    graph = get_graph(input_filename)

    shortest_paths = find_shortest_paths(graph)

    actual = [shortest_paths[i] for i in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]]

    assert actual == expected
