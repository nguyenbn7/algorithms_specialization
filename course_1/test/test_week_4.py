from sys import path as sys_path
from os import path as os_path

# Resolve for parent module
current = os_path.dirname(os_path.realpath(__file__))
sys_path.append(os_path.join(current, ".."))

from src.week_4 import min_cut


def test_sample_1():
    answer = 2
    graph = {}

    with open(os_path.join(current, "../input/week_4/sample_1.txt"), "r") as f:
        lines = f.readlines()
        for line in lines:
            temp = list(map(int, line.split()))
            graph[temp[0]] = temp[1:]

    attempt = min_cut(graph)

    assert attempt == answer


def test_sample_2():
    answer = 2
    graph = {}

    with open(os_path.join(current, "../input/week_4/sample_2.txt"), "r") as f:
        lines = f.readlines()
        for line in lines:
            temp = list(map(int, line.split()))
            graph[temp[0]] = temp[1:]

    attempt = min_cut(graph)

    assert attempt == answer


def test_question():
    answer = 17
    graph = {}

    with open(os_path.join(current, "../input/week_4/question.txt"), "r") as f:
        lines = f.readlines()
        for line in lines:
            temp = list(map(int, line.split()))
            graph[temp[0]] = temp[1:]

    attempt = min_cut(graph)

    assert attempt == answer
