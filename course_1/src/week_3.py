from enum import Enum
from typing import List


class PivotPartitionStyles(Enum):
    first_element = 1
    last_element = 2
    median_of_three = 3


def count_comparisions_quick_sort(
    arr: List[int],
    left: int,
    right: int,
    partition_style: PivotPartitionStyles = PivotPartitionStyles.median_of_three,
) -> int:
    """
    Count how many comparisions during quick sort if using median of three for pivot partition
    """

    if left >= right:
        return 0

    c = right - left

    pivot = __pivot_partition(arr, left, right, partition_style)

    c += count_comparisions_quick_sort(arr, left, pivot - 1, partition_style)
    c += count_comparisions_quick_sort(arr, pivot + 1, right, partition_style)

    return c


def __pivot_partition(
    arr: List[int],
    left: int,
    right: int,
    partition_style: PivotPartitionStyles = PivotPartitionStyles.median_of_three,
) -> int:
    if partition_style == PivotPartitionStyles.median_of_three:
        mid = left + (right - left) // 2
        # https://stackoverflow.com/questions/1582356/fastest-way-of-finding-the-middle-value-of-a-triple/14676309#14676309
        if (arr[left] - arr[mid]) * (arr[right] - arr[left]) >= 0:
            median = left
        elif (arr[mid] - arr[left]) * (arr[right] - arr[mid]) >= 0:
            median = mid
        else:
            median = right
        arr[left], arr[median] = arr[median], arr[left]

    elif partition_style == PivotPartitionStyles.last_element:
        arr[left], arr[right] = arr[right], arr[left]

    pivot = arr[left]
    j = left + 1

    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    arr[left], arr[j - 1] = arr[j - 1], arr[left]
    return j - 1


if __name__ == "__main__":
    from pathlib import Path
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "txt_file", help="Text file contains numbers seperated by new line", type=str
    )

    args = parser.parse_args()

    filepath: str = args.txt_file

    input_file = (Path.cwd() / filepath).resolve()

    with open(
        input_file,
        "r",
    ) as f:
        numbers = list(map(int, f.readlines()))

    print(
        "Using last element:",
        count_comparisions_quick_sort(
            numbers.copy(), 0, len(numbers) - 1, PivotPartitionStyles.last_element
        ),
    )

    print(
        "Using first element:",
        count_comparisions_quick_sort(
            numbers.copy(), 0, len(numbers) - 1, PivotPartitionStyles.first_element
        ),
    )

    print(
        "Using Median of three:",
        count_comparisions_quick_sort(
            numbers.copy(), 0, len(numbers) - 1, PivotPartitionStyles.median_of_three
        ),
    )
