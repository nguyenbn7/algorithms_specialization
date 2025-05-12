from pathlib import Path

import pytest
import test as _

from src.week_3 import count_comparisions_quick_sort, PivotPartitionStyles


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
        numbers = list(map(int, f.readlines()))

    return numbers


def get_expected_test_result(filename):
    with open(
        output_test_path / filename,
        "r",
    ) as f:
        return list(map(int, f.readlines()))


@pytest.mark.parametrize(
    "input_filename,output_filename",
    [*zip(input_test_filenames, output_test_filenames)],
)
def test_total_number_of_comparisons_used_to_sort_by_quick_sort_using(
    input_filename, output_filename
):
    expected = get_expected_test_result(output_filename)

    numbers = get_numbers(input_filename)

    first_ele = count_comparisions_quick_sort(
        numbers.copy(), 0, len(numbers) - 1, PivotPartitionStyles.first_element
    )

    last_ele = count_comparisions_quick_sort(
        numbers.copy(), 0, len(numbers) - 1, PivotPartitionStyles.last_element
    )

    median_of_three = count_comparisions_quick_sort(
        numbers.copy(), 0, len(numbers) - 1, PivotPartitionStyles.median_of_three
    )

    assert [first_ele, last_ele, median_of_three] == expected
