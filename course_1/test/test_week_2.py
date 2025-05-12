from pathlib import Path

import pytest
import test as _

from src.week_2 import count_inversion


current_path = Path(__file__).parent.resolve()

input_test_path = current_path / "input/week_2"
input_test_filenames = [f.name for f in input_test_path.glob("*.txt")]

output_test_path = current_path / "output/week_2"
output_test_filenames = [f.name for f in output_test_path.glob("*.txt")]


def get_numbers(filename: str):
    with open(
        input_test_path / filename,
        "r",
    ) as f:
        numbers = list(map(int, f.readlines()))

    return numbers


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
def test_count_inversion(input_filename, output_filename):
    expected = get_expected_test_result(output_filename)

    numbers = get_numbers(input_filename)

    actual = count_inversion(numbers, [None] * len(numbers), 0, len(numbers) - 1)

    assert actual == expected
