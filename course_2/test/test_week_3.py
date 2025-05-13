from pathlib import Path

import pytest
import test as _

from src.week_3 import find_median_maintenance

current_path = Path(__file__).parent.resolve()

input_test_path = current_path / "input/week_3"
input_test_filenames = [f.name for f in input_test_path.glob("*.txt")]

output_test_path = current_path / "output/week_3"
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
def test_median_maintenance(input_filename, output_filename):
    expected = get_expected_test_result(output_filename)

    numbers = get_numbers(input_filename)

    sum_median = find_median_maintenance(numbers)

    actual = sum_median % 10_000

    assert actual == expected
