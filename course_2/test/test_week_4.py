from pathlib import Path

import pytest
import test as _

from src.week_4 import get_number_of_target_from_2_distinct_numbers

current_path = Path(__file__).parent.resolve()

input_test_path = current_path / "input/week_4"
input_test_filenames = [f.name for f in input_test_path.glob("*.txt")]

output_test_path = current_path / "output/week_4"
output_test_filenames = [f.name for f in output_test_path.glob("*.txt")]


def get_numbers(filename: str):
    with open(
        input_test_path / filename,
        "r",
    ) as f:
        return list(map(int, f.readlines()))


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
def test_2_sum_interval(input_filename, output_filename):
    expected = get_expected_test_result(output_filename)

    numbers = get_numbers(input_filename)

    actual = get_number_of_target_from_2_distinct_numbers(numbers)

    assert actual == expected
