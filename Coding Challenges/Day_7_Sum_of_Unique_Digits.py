# Day 7: Sum of Unique Digits
# 
# Problem Statement:
# Given an integer N, find the sum of its unique digits.
# 
# Input:
# - A single integer N (can be positive or negative)
# 
# Output:
# - An integer representing the sum of unique digits in N.
# 
# Example 1:
# Input:  122333
# Output: 6  # (1 + 2 + 3)
# 
# Example 2:
# Input:  987656789
# Output: 30  # (9 + 8 + 7 + 6 + 5)
# 
# Example 3:
# Input:  -112233
# Output: 6  # (1 + 2 + 3)
# 
# Constraints:
# - The input number can be negative, but only digits are considered.
# - The number will not exceed 10^9 in absolute value.

def sum_of_unique_digits(n):
    n = abs(n)  # Convert to positive to ignore the sign
    unique_digits = set(str(n))  # Extract unique digits
    return sum(int(digit) for digit in unique_digits)

# Example test cases
print(sum_of_unique_digits(122333))  # Output: 6
print(sum_of_unique_digits(987656789))  # Output: 30
print(sum_of_unique_digits(-112233))  # Output: 6
