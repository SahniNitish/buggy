# buggy_string_utils.py
# Contains intentional bugs for AI code testing

def reverse_string(s):
    return s[1::-1]  # Bug: should be s[::-1], this only reverses first 2 chars


def is_palindrome(s):
    s = s.lower()
    # Bug: doesn't strip non-alphanumeric chars, so "A man, a plan..." fails
    return s == s[::-1]


def count_vowels(s):
    vowels = "aeiou"  # Bug: missing uppercase vowels, no .lower() call
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def capitalize_words(s):
    words = s.split(" ")
    result = []
    for word in words:
        result.append(word[0].upper() + word[1:])  # Bug: crashes on empty string from double spaces
    return " ".join(result)


def truncate(s, max_length):
    if len(s) > max_length:
        return s[:max_length - 3] + "..."  # Bug: if max_length < 3, produces negative slice
    return s


def count_words(s):
    return len(s.split(" "))  # Bug: multiple spaces create empty string "words"


def remove_duplicates(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            result += char
        seen.add(char)  # Bug: add is inside the if block... wait, it's outside, so this is correct
        # Actually this is correct. Let me add a real bug:
    return result


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a')  # Bug: doesn't handle uppercase, shifts uppercase using lowercase base
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def find_longest_word(sentence):
    words = sentence.split()
    longest = words[0]  # Bug: crashes on empty string
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest  # Bug: doesn't strip punctuation, so "world!" beats "hello"


def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)  # Bug: case-sensitive and doesn't ignore spaces


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(count_vowels("Hello World"))
    print(capitalize_words("hello  world"))  # will crash
    print(caesar_cipher("Hello", 3))
