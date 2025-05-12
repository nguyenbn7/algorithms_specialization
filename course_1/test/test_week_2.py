from sys import path as sys_path
from os import path as os_path

# Resolve for parent module
current = os_path.dirname(os_path.realpath(__file__))
sys_path.append(os_path.join(current, ".."))

from src.week_2 import count_inversion


def test_question():
    answer = 2407905288

    with open(os_path.join(current, "../input/week_2/question.txt"), "r") as f:
        numbers = list(map(int, f.readlines()))

    attempt = count_inversion(numbers, [None] * len(numbers), 0, len(numbers) - 1)

    assert attempt == answer
