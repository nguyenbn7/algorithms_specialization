from pathlib import Path

import pytest
import test as _

from src.week_1 import find_scc

current_path = Path(__file__).parent.resolve()

input_test_path = current_path / "input/week_1"
input_test_filenames = [f.name for f in input_test_path.glob("*.txt")]

output_test_path = current_path / "output/week_1"
output_test_filenames = [f.name for f in output_test_path.glob("*.txt")]


def get_graph(filename: str):
    with open(
        input_test_path / filename,
        "r",
    ) as f:
        lines = f.readlines()

        data = [tuple(map(lambda x: int(x), l.split())) for l in lines]

        len_graph = max(max(data)) + 1

        graph = [[] for _ in range(len_graph)]
        rev_graph = [[] for _ in range(len_graph)]

        for v, e in data:
            graph[v].append(e)
            rev_graph[e].append(v)

    return (graph, rev_graph, len_graph)


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
def test_scc(input_filename, output_filename):
    expected = get_expected_test_result(output_filename)

    (graph, rev_graph, len_graph) = get_graph(input_filename)

    scc = find_scc(graph, rev_graph, len_graph)

    scc.sort(reverse=True)

    actual = scc[:5]

    assert actual == expected
