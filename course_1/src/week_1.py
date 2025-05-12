def karatsuba(num1: int, num2: int) -> int:
    """
    Fast algorithm Karatsuba for multiply 2 big numbers
    """

    if num1 < 10 or num2 < 10:
        return num1 * num2  # fall back to traditional multiplication

    # Calculates the size of the numbers.
    min_num = min(len(str(num1)), len(str(num2)))
    m2 = min_num // 2  # floor or ceilt works fine
    base = 10**m2

    # Split the digit sequences in the middle.
    high1, low1 = num1 // base, num1 % base
    high2, low2 = num2 // base, num2 % base

    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return z2 * 10 ** (m2 * 2) + ((z1 - z2 - z0) * 10**m2) + z0


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
        num1, num2 = map(int, f.readlines())

    print(karatsuba(num1, num2))
