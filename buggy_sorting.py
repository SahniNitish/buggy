# buggy_sorting.py
# Contains intentional bugs for AI code testing

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):  # Bug: should be n - 1 - i for optimization, but real bug below
            if arr[j] > arr[j + 1]:
                arr[j] = arr[j + 1]  # Bug: swaps incorrectly, overwrites arr[j] before saving it
                arr[j + 1] = arr[j]
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Bug: only appends remaining from left, forgets right
    result.extend(left[i:])
    # Missing: result.extend(right[j:])
    return result


def binary_search(arr, target):
    low, high = 0, len(arr)  # Bug: should be len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:  # Bug: can cause IndexError when high == len(arr)
            return mid
        elif arr[mid] < target:
            low = mid  # Bug: should be mid + 1, causes infinite loop
        else:
            high = mid - 1
    return -1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j] = key  # Bug: should be arr[j + 1] = key (off-by-one)
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]  # Bug: loses elements equal to pivot (except first)
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    print(bubble_sort([5, 3, 8, 1, 2]))
    print(merge_sort([5, 3, 8, 1, 2]))
    print(binary_search([1, 2, 3, 4, 5], 3))
    print(insertion_sort([5, 3, 8, 1, 2]))
    print(quick_sort([5, 3, 8, 1, 2, 5, 5]))
