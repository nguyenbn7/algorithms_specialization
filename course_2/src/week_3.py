import heapq
from typing import List


def rebalance(h_low: List[int], h_high: List[int]):
    diff = len(h_low) - len(h_high)
    if diff == 2:
        h_low_max_ele = heapq.nlargest(1, h_low)[0]
        h_low.remove(h_low_max_ele)
        heapq.heapify(h_low)
        heapq.heappush(h_high, -h_low_max_ele)
    elif diff == -1:
        h_high_min_ele = heapq.nlargest(1, h_high)[0]
        h_high.remove(h_high_min_ele)
        heapq.heapify(h_high)
        heapq.heappush(h_low, -h_high_min_ele)
    elif diff == 0 or diff == 1:
        pass
    else:
        raise Exception("size between 2 heaps are greater than 2 or less than -2")


def find_median_maintenance(numbers: List[int]):
    # Extract Max
    h_low = []
    # Extract Min
    h_high = []
    # Record medians
    medians = []

    for num in numbers:
        if not h_low or num < heapq.nlargest(1, h_low)[0]:
            heapq.heappush(h_low, num)
        else:
            heapq.heappush(h_high, -num)

        rebalance(h_low, h_high)
        medians.append(heapq.nlargest(1, h_low)[0])

    return sum(medians)


if __name__ == "__main__":
    from pathlib import Path
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "txt_file", help="Text file contains 2 numbers seperated by new line", type=str
    )

    args = parser.parse_args()

    filepath: str = args.txt_file

    input_file = (Path.cwd() / filepath).resolve()

    with open(
        input_file,
        "r",
    ) as f:
        numbers = list(map(int, f.readlines()))

    sum_medians = find_median_maintenance(numbers)

    print(sum_medians % 10_000)
