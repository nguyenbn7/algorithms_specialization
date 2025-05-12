"""
Test case at https://www.coursera.org/learn/algorithms-divide-conquer/discussions/forums/CXME63blEeahNRJMZJSNzw/threads/mFg8lpQHEeaQYRKcXQcKHQ
"""

from sys import path as sys_path
from os import path as os_path

# Resolve for parent module
current = os_path.dirname(os_path.realpath(__file__))
sys_path.append(os_path.join(current, ".."))

from src.week_2 import count_inversion


def get_numbers(filename: str):
    with open(os_path.join(current, f"../input/week_2/{filename}"), "r") as f:
        numbers = list(map(int, f.readlines()))

    return numbers


def test_case_1():
    answer = 3

    numbers = get_numbers("test_1.txt")

    attempt = count_inversion(numbers, [None] * len(numbers), 0, len(numbers) - 1)

    assert attempt == answer


def test_case_2():
    answer = 4

    numbers = get_numbers("test_2.txt")

    attempt = count_inversion(numbers, [None] * len(numbers), 0, len(numbers) - 1)

    assert attempt == answer


def test_case_3():
    answer = 10

    numbers = get_numbers("test_3.txt")

    attempt = count_inversion(numbers, [None] * len(numbers), 0, len(numbers) - 1)

    assert attempt == answer


def test_case_4():
    answer = 5

    numbers = get_numbers("test_4.txt")

    attempt = count_inversion(numbers, [None] * len(numbers), 0, len(numbers) - 1)

    assert attempt == answer


def test_case_5():
    answer = 56

    numbers = get_numbers("test_5.txt")

    attempt = count_inversion(numbers, [None] * len(numbers), 0, len(numbers) - 1)

    assert attempt == answer


def test_case_6():
    answer = 590

    numbers = get_numbers("test_6.txt")

    attempt = count_inversion(numbers, [None] * len(numbers), 0, len(numbers) - 1)

    assert attempt == answer


def test_case_7():
    answer = 2372

    numbers = get_numbers("test_7.txt")

    attempt = count_inversion(numbers, [None] * len(numbers), 0, len(numbers) - 1)

    assert attempt == answer
