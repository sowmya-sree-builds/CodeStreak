# Day 27: Sum of Even Numbers in a List

def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# Example usage
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Sum of even numbers:", sum_of_evens(nums))
