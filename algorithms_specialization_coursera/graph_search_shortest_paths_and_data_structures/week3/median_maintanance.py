import heapq
from typing import List

# Extract Max
h_low = []
# Extract Min
h_high = []
# Record medians
medians = []


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


with open("./test2.txt") as file:
    for num_str in file:
        num = int(num_str)
        if not h_low or num < heapq.nlargest(1, h_low)[0]:
            heapq.heappush(h_low, num)
        else:
            heapq.heappush(h_high, -num)

        rebalance(h_low, h_high)
        medians.append(heapq.nlargest(1, h_low)[0])

print(sum(medians) % 10000)
