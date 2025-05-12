from pathlib import Path

import pytest
import test as _

from src.week_1 import karatsuba


current_path = Path(__file__).parent.resolve()

input_test_path = current_path / "input/week_1"
input_test_filenames = [f.name for f in input_test_path.glob("*.txt")]

output_test_path = current_path / "output/week_1"
output_test_filenames = [f.name for f in output_test_path.glob("*.txt")]


def get_numbers(filename: str):
    with open(
        input_test_path / filename,
        "r",
    ) as f:
        num1, num2 = map(int, f.readlines())

    return (num1, num2)


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
def test_karatsuba_multiplication(input_filename, output_filename):
    expected = get_expected_test_result(output_filename)

    (num1, num2) = get_numbers(input_filename)

    actual = karatsuba(num1, num2)

    assert actual == expected
