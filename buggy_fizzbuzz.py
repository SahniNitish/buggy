# buggy_fizzbuzz.py
# Contains intentional bugs for AI code testing demos — now fixed

def fizzbuzz(n):
    results = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results


# ---- Tests that will fail ----
if __name__ == "__main__":
    output = fizzbuzz(15)
    assert output[14] == "FizzBuzz", f"Expected FizzBuzz at 15, got {output[14]}"
    assert output[2]  == "Fizz",    f"Expected Fizz at 3, got {output[2]}"
    assert output[4]  == "Buzz",    f"Expected Buzz at 5, got {output[4]}"
    print("All tests passed!")