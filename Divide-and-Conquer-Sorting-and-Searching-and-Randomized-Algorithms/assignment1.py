def karatsuba(num1: int, num2: int) -> int:
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
