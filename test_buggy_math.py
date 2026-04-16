import pytest
from buggy_math import calculate_average, is_prime, celsius_to_fahrenheit, factorial, find_max


class TestCalculateAverage:
    def test_simple_average(self):
        assert calculate_average([10, 20, 30]) == 20

    def test_single_value(self):
        assert calculate_average([7]) == 7

    def test_float_result(self):
        assert calculate_average([1, 2]) == 1.5


class TestIsPrime:
    def test_less_than_two(self):
        assert is_prime(0) is False
        assert is_prime(1) is False
        assert is_prime(-5) is False

    def test_primes(self):
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(13) is True
        assert is_prime(97) is True

    def test_composites(self):
        assert is_prime(4) is False
        assert is_prime(9) is False
        assert is_prime(100) is False


class TestCelsiusToFahrenheit:
    def test_freezing(self):
        assert celsius_to_fahrenheit(0) == 32

    def test_boiling(self):
        assert celsius_to_fahrenheit(100) == 212

    def test_negative(self):
        assert celsius_to_fahrenheit(-40) == -40


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_five(self):
        assert factorial(5) == 120

    def test_ten(self):
        assert factorial(10) == 3628800


class TestFindMax:
    def test_simple(self):
        assert find_max([3, 1, 4, 1, 5]) == 5

    def test_all_equal(self):
        assert find_max([7, 7, 7]) == 7

    def test_negative_numbers(self):
        assert find_max([-3, -1, -4, -1, -5]) == -1