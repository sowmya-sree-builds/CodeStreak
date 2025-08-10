# Day 26: Sum of Digits in a Range (Simple Loop Method)

def sum_of_digits(num):
    """Returns sum of digits of a single number."""
    total = 0
    while num > 0:
        total += num % 10  # get last digit
        num //= 10         # remove last digit
    return total

def sum_of_digits_in_range(L, R):
    """Returns sum of digits from L to R."""
    total_sum = 0
    for i in range(L, R + 1):
        total_sum += sum_of_digits(i)
    return total_sum

# Example usage:
if __name__ == "__main__":
    L, R = map(int, input("Enter L and R: ").split())
    result = sum_of_digits_in_range(L, R)
    print(f"Sum of digits from {L} to {R} is: {result}")
