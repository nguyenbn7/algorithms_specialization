from math import log10, ceil
from typing import List, Tuple


def get_number_of_target_from_2_distinct_numbers(
    numbers: List[int], interval: Tuple[int, int] = (-10_000, 10_000)
):

    (min_target, max_target) = interval

    tables = {}

    scale = 10 ** ceil(log10(max_target - min_target))

    s = set()

    for num in numbers:
        quo, rem = divmod(num, scale)

        if quo not in tables:
            tables[quo] = set([rem])
        else:
            tables[quo].add(rem)

        min_quo, _ = divmod(min_target - num, scale)
        max_quo, _ = divmod(max_target - num, scale)

        if min_quo in tables:
            for remainder in tables[min_quo]:
                temp = min_quo * scale + remainder + num
                if min_target <= temp <= max_target:
                    s.add(temp)

        if max_quo in tables:
            for remainder in tables[max_quo]:
                temp = max_quo * scale + remainder + num
                if min_target <= temp <= max_target:
                    s.add(temp)

    return len(s)


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

    print(get_number_of_target_from_2_distinct_numbers(numbers))
