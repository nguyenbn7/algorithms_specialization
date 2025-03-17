from typing import List


def count_inversion(arr: List[int], temp: List[int], left: int, right: int) -> int:
    if left >= right:
        return 0
    c = 0
    mid = left + (right - left) // 2
    c += count_inversion(arr, temp, left, mid)
    c += count_inversion(arr, temp, mid + 1, right)
    c += __merge_and_count_split_inversion(arr, temp, left, mid + 1, right)
    return c


def __merge_and_count_split_inversion(
    arr: List[int], temp: List[int], left: int, mid: int, right: int
) -> int:
    i, j, k, c = left, mid, left, 0

    while (i <= mid - 1) and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
            c += mid - i

    while i <= mid - 1:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return c
