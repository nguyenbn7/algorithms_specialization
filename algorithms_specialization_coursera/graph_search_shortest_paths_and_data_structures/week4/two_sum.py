from math import log10, ceil

min_target = -10_000
max_target = 10_000

tables = {}

scale = 10 ** ceil(log10(max_target - min_target))

s = set()

with open("./input.txt") as file:
    for num_str in file:
        num = int(num_str)
        quo, rem = divmod(num, scale)

        if quo not in tables:
            tables[quo] = set([rem])
        else:
            tables[quo].add(rem)

        a = set()
        b = set()
        min_quo, min_rem = divmod(min_target - num, scale)
        max_quo, max_rem = divmod(max_target - num, scale)

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

print(len(s))
