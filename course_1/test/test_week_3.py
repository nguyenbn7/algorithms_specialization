from sys import path as sys_path
from os import path as os_path

# Resolve for parent module
current = os_path.dirname(os_path.realpath(__file__))
sys_path.append(os_path.join(current, ".."))

from src.week_3 import count_comparisions_quick_sort, PivotPartitionStyles


def test_question_median_of_three():
    answer = 138382

    with open(os_path.join(current, "../input/week_3/question.txt"), "r") as f:
        numbers = list(map(int, f.readlines()))

    attempt = count_comparisions_quick_sort(numbers, 0, len(numbers) - 1)

    assert attempt == answer


def test_question_first_element():
    answer = 162085

    with open(os_path.join(current, "../input/week_3/question.txt"), "r") as f:
        numbers = list(map(int, f.readlines()))

    attempt = count_comparisions_quick_sort(
        numbers, 0, len(numbers) - 1, PivotPartitionStyles.first_element
    )

    assert attempt == answer


def test_question_last_element():
    answer = 164123

    with open(os_path.join(current, "../input/week_3/question.txt"), "r") as f:
        numbers = list(map(int, f.readlines()))

    attempt = count_comparisions_quick_sort(
        numbers, 0, len(numbers) - 1, PivotPartitionStyles.last_element
    )

    assert attempt == answer
