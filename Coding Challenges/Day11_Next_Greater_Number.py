# Day 11: Digit Rearrangement Game

from itertools import permutations

def next_greater_number(n):
    """
    Function to find the next greater number using the digits of N.

    Parameters:
    n (int): The input number.

    Returns:
    int: The next greater number, or -1 if not possible.
    """
    # Convert number to list of digits
    digits = list(str(n))
    
    # Find the next permutation in lexicographical order
    for perm in sorted(permutations(digits)):
        num = int("".join(perm))
        if num > n:
            return num
    
    return -1

# Example test cases
print(next_greater_number(218))   # Output: 281
print(next_greater_number(4321))  # Output: -1
print(next_greater_number(1234))  # Output: 1243
print(next_greater_number(998))   # Output: -1
