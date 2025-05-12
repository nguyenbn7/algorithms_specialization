from pathlib import Path

import pytest
import test as _

from src.week_4 import min_cut, Edge, Graph


current_path = Path(__file__).parent.resolve()

input_test_path = current_path / "input/week_4"
input_test_filenames = [f.name for f in input_test_path.glob("*.txt")]

output_test_path = current_path / "output/week_4"
output_test_filenames = [f.name for f in output_test_path.glob("*.txt")]


def get_graph(filename: str):
    graph = Graph(0, 0)

    with open(
        input_test_path / filename,
        "r",
    ) as f:
        lines = f.readlines()
        for line in lines:
            temp = list(map(int, line.split()))

            graph.no_vertex += 1
            graph.no_edge += len(temp[1:])

            for dest in temp[1:]:
                graph.edges.append(Edge(temp[0], dest))

    return graph


def get_expected_test_result(filename):
    with open(
        output_test_path / filename,
        "r",
    ) as f:
        return int(f.readline())


@pytest.mark.parametrize(
    "input_filename,output_filename",
    [*zip(input_test_filenames, output_test_filenames)],
)
def test_karger_min_cut(input_filename, output_filename):
    expected = get_expected_test_result(output_filename)

    graph = get_graph(input_filename)

    actual = min_cut(graph)

    assert actual == expected
