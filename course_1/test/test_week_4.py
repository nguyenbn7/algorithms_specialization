from sys import path as sys_path
from os import path as os_path

# Resolve for parent module
current = os_path.dirname(os_path.realpath(__file__))
sys_path.append(os_path.join(current, ".."))

from src.week_4 import min_cut


def get_graph(filename: str):
    graph = {}

    with open(os_path.join(current, f"../input/week_4/{filename}"), "r") as f:
        lines = f.readlines()
        for line in lines:
            temp = list(map(int, line.split()))
            graph[temp[0]] = temp[1:]

    return graph


def test_sample_1():
    answer = 2

    graph = get_graph("sample_1.txt")

    attempt = min_cut(graph)

    assert attempt == answer


def test_sample_2():
    answer = 2

    graph = get_graph("sample_2.txt")

    attempt = min_cut(graph)

    assert attempt == answer


def test_question():
    answer = 17

    graph = get_graph("question.txt")

    attempt = min_cut(graph)

    assert attempt == answer
