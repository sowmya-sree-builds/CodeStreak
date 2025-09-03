# Day 34: Program to find the next prime number after a given number

def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(n):
    """Find the next prime greater than n"""
    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1

# Example runs
print(next_prime(20))  # Output: 23
print(next_prime(7))   # Output: 11
print(next_prime(2))   # Output: 3
