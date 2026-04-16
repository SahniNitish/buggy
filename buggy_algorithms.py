# buggy_algorithms.py
# Contains intentional bugs for AI code testing

def fibonacci(n):
    """Return nth Fibonacci number."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
    # Bug: no memoization, O(2^n) time — will hang for n > 35


def gcd(a, b):
    """Greatest common divisor."""
    while b != 0:
        a = b  # Bug: should be a, b = b, a % b — this just sets a = b then loops
        b = a % b
    return a


def power(base, exp):
    """Calculate base^exp."""
    result = 0  # Bug: should be 1 (multiplicative identity)
    for _ in range(exp):
        result *= base
    return result


def flatten(nested_list):
    """Flatten a nested list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.append(flatten(item))  # Bug: should be extend, not append
        else:
            result.append(item)
    return result


def matrix_multiply(a, b):
    """Multiply two matrices."""
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    # Bug: doesn't check that cols_a == rows_b
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result
    # This one is actually correct — keeping for completeness


def two_sum(nums, target):
    """Find two indices that add up to target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # Bug: should return None or raise, empty list is truthy confusion


def remove_duplicates_sorted(arr):
    """Remove duplicates from a sorted array in-place."""
    if not arr:
        return 0
    write_idx = 0
    for read_idx in range(1, len(arr)):
        if arr[read_idx] != arr[write_idx]:
            write_idx += 1
            arr[write_idx] = arr[read_idx]
    return write_idx  # Bug: should return write_idx + 1 (length, not last index)


def is_balanced_parens(s):
    """Check if parentheses are balanced."""
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
    return count == 0
    # Bug: doesn't detect ")(" — count ends at 0 but parens aren't balanced
    # Should check if count ever goes negative


def rotate_array(arr, k):
    """Rotate array to the right by k positions."""
    n = len(arr)
    k = k % n  # good
    return arr[k:] + arr[:k]  # Bug: rotates LEFT, not right. Should be arr[n-k:] + arr[:n-k]


def kadane_max_subarray(arr):
    """Find maximum subarray sum using Kadane's algorithm."""
    max_sum = 0  # Bug: fails for all-negative arrays, should be float('-inf')
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum


if __name__ == "__main__":
    print(gcd(12, 8))
    print(power(2, 10))  # Expect 1024, get 0
    print(flatten([1, [2, [3, 4], 5]]))
    print(is_balanced_parens(")("))  # Expect False, get True
    print(rotate_array([1, 2, 3, 4, 5], 2))  # Expect [4,5,1,2,3], get [3,4,5,1,2]
    print(kadane_max_subarray([-2, -3, -1, -5]))  # Expect -1, get 0
