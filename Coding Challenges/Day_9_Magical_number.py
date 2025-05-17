# Day 9: TCS NQT Question - Magical Number
#
# Problem Statement:
# A number is called **magical** if the sum of its digits, when repeatedly 
# added, results in a single-digit number. Find whether a given number is 
# magical or not.
#
# Steps:
# 1. Find the sum of the digits of the number.
# 2. If the sum is a single-digit number, check if it's equal to 1.
# 3. If not, repeat the process with the new sum until we get a single-digit number.
# 4. If the final single-digit sum is 1, it's a **Magical Number**; otherwise, it's **Not Magical**.
#
# Input:
# - An integer N (1 ≤ N ≤ 10^9)
#
# Output:
# - "Magical" if the final sum is 1, otherwise "Not Magical".
#
# Example 1:
# Input:  19
# Output: Magical
#
# Explanation:
# 1 + 9 = 10
# 1 + 0 = 1  --> It is a magical number.
#
# Example 2:
# Input:  123
# Output: Not Magical
#
# Explanation:
# 1 + 2 + 3 = 6  --> It is not 1, so it's not magical.

def is_magical_number(n):
    """
    Function to check whether a number is magical or not.

    Parameters:
    n (int): The input number.

    Returns:
    str: "Magical" if the number is magical, otherwise "Not Magical".
    """
    
    # Keep reducing the number until it becomes a single digit
    while n >= 10:
        # Convert the number to a string, extract each digit, convert to integer, and sum them up
        n = sum(int(digit) for digit in str(n))
        # Print intermediate steps for better understanding (optional for debugging)
        print(f"Intermediate sum: {n}")

    # If the final sum is 1, return "Magical", otherwise return "Not Magical"
    return "Magical" if n == 1 else "Not Magical"

# Example test cases
print(is_magical_number(19))   # Output: Magical
print(is_magical_number(123))  # Output: Not Magical
print(is_magical_number(9875)) # Output: Magical
print(is_magical_number(28))   # Output: Not Magical
