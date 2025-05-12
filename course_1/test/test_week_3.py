from sys import path as sys_path
from os import path as os_path

# Resolve for parent module
current = os_path.dirname(os_path.realpath(__file__))
sys_path.append(os_path.join(current, ".."))

from src.week_3 import count_comparisions_quick_sort, PivotPartitionStyles


def get_numbers(filename: str):
    with open(os_path.join(current, f"../input/week_3/{filename}"), "r") as f:
        numbers = list(map(int, f.readlines()))

    return numbers


def test_question_median_of_three():
    answer = 138382

    numbers = get_numbers("question.txt")

    attempt = count_comparisions_quick_sort(numbers, 0, len(numbers) - 1)

    assert attempt == answer


def test_question_first_element():
    answer = 162085

    numbers = get_numbers("question.txt")

    attempt = count_comparisions_quick_sort(
        numbers, 0, len(numbers) - 1, PivotPartitionStyles.first_element
    )

    assert attempt == answer


def test_question_last_element():
    answer = 164123

    numbers = get_numbers("question.txt")

    attempt = count_comparisions_quick_sort(
        numbers, 0, len(numbers) - 1, PivotPartitionStyles.last_element
    )

    assert attempt == answer
