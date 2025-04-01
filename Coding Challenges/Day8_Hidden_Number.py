# Day 8: Hidden Number in a String
#
# Problem Statement:
# Given a string containing alphabets and digits, extract all digits, 
# form the largest possible number using those digits, and return it.
#
# Input:
# - A string S (1 ≤ len(S) ≤ 100) containing alphabets and digits.
#
# Output:
# - An integer representing the largest number that can be formed.
#
# Example 1:
# Input:  "a5b3c9"
# Output: 953
#
# Example 2:
# Input:  "xyz123"
# Output: 321
#
# Example 3:
# Input:  "abc"
# Output: 0  # No digits present
#
# Constraints:
# - The input string contains at least one character.
# - If no digits are found, return 0.

def largest_number_from_string(s):
    digits = [char for char in s if char.isdigit()]
    if not digits:
        return 0
    return int("".join(sorted(digits, reverse=True)))

# Example test cases
print(largest_number_from_string("a5b3c9"))  # Output: 953
print(largest_number_from_string("xyz123"))  # Output: 321
print(largest_number_from_string("abc"))     # Output: 0
