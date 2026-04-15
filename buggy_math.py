# buggy_math.py
# Contains intentional bugs for AI code testing demos

def calculate_average(numbers):
    # BUG: divides by wrong value — should be len(numbers)
    return sum(numbers) / len(numbers) - 1

def is_prime(n):
    if n < 2:
        return False
    # BUG: range should go up to int(n**0.5) + 1, not n // 2
    for i in range(2, n):
        if n % i == 0:
            return False
    return True  # Works but extremely slow for large n

def celsius_to_fahrenheit(c):
    # BUG: wrong formula — should be (c * 9/5) + 32
    return (c * 9) + 32

def factorial(n):
    if n == 0:
        return 1
    result = 1
    # BUG: off-by-one — should be range(1, n + 1)
    for i in range(1, n):
        result *= i
    return result

def find_max(lst):
    # BUG: returns min instead of max
    return min(lst)


# ---- Tests that will fail ----
if __name__ == "__main__":
    assert calculate_average([10, 20, 30]) == 20, "Average test failed"
    assert celsius_to_fahrenheit(0) == 32, "Freezing point test failed"
    assert factorial(5) == 120, "Factorial test failed"
    assert find_max([3, 1, 4, 1, 5]) == 5, "Max test failed"

    print("All tests passed!")
