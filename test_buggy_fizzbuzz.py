import pytest
from buggy_fizzbuzz import fizzbuzz


class TestFizzBuzz:
    def test_fifteen_produces_fizzbuzz(self):
        output = fizzbuzz(15)
        assert output[14] == "FizzBuzz"

    def test_three_produces_fizz(self):
        output = fizzbuzz(15)
        assert output[2] == "Fizz"

    def test_five_produces_buzz(self):
        output = fizzbuzz(15)
        assert output[4] == "Buzz"

    def test_one_produces_number(self):
        output = fizzbuzz(15)
        assert output[0] == "1"

    def test_full_sequence(self):
        expected = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz",
        ]
        assert fizzbuzz(15) == expected

    def test_thirty_includes_fizzbuzz(self):
        output = fizzbuzz(30)
        assert output[14] == "FizzBuzz"
        assert output[29] == "FizzBuzz"