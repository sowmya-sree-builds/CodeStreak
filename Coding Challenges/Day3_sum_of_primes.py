"""
Problem Statement: Sum of All Prime Numbers

Given an integer n, return the sum of all prime numbers between 2 and n (inclusive).

Constraints:
2 ≤ n < 10

Input:
- A single integer n representing the upper limit.

Output:
- Return an integer representing the sum of all prime numbers between 2 and n.

Example 1:
Input: 10
Output: 17
Explanation: The prime numbers between 2 and 10 are (2, 3, 5, 7). Their sum is 2 + 3 + 5 + 7 = 17.

Example 2:
Input: 2
Output: 2
Explanation: 2 is the only prime number between 2 and 2.
"""

import math

def is_prime(num):
    """Checks if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    """Returns the sum of all prime numbers from 2 to n (inclusive)"""
    return sum(num for num in range(2, n + 1) if is_prime(num))

# Example usage
n = int(input("Enter n: "))

if n < 2 or n >= 10:
    print("Invalid input: n should be in the range 2 ≤ n < 10")
else:
    print(sum_of_primes(n))
 
