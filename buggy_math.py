# buggy_math.py
# Contains intentional bugs for AI code testing demos — now fixed

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def find_max(lst):
    return max(lst)


# ---- Tests that will fail ----
if __name__ == "__main__":
    assert calculate_average([10, 20, 30]) == 20, "Average test failed"
    assert celsius_to_fahrenheit(0) == 32, "Freezing point test failed"
    assert factorial(5) == 120, "Factorial test failed"
    assert find_max([3, 1, 4, 1, 5]) == 5, "Max test failed"

    print("All tests passed!")