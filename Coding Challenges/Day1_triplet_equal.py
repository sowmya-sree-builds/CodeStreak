# Complexity: Medium
# This Question has been Asked on TCS NQT 15-03-2025
#  Problem: Making Triplets Equal
# You are given a triplet of integers (a, b, c). You can perform the following operation any number of times:
# 1. Select any two numbers from the triplet.
# 2. Add 1 to both selected numbers.
# 3. Subtract 1 from the remaining number.
# Your task is to determine whether it is possible to make all three numbers equal using the given operations.
#
# Input:
# A single integer T representing the number of test cases.
# Each test case consists of three integers a, b, c.
#
# Output:
# For each test case, print "YES" if it is possible to make all three numbers equal; otherwise, print "NO".
#
# Constraints:
# 1 <= T <= 10^3
# 1 <= a, b, c <= 10^3
#
# Example:
# Input:
# 3
# 1 2 3
# 4 4 4
# 3 3 7
#
# Output:
# 1
# 0
# -1

# Function to determine the minimum steps to make the triplet equal
def min_steps_to_equal(P, Q, R):
    arr = [P, Q, R]
    arr.sort()
    
    # If all numbers are already equal
    if arr[0] == arr[1] == arr[2]:
        return 0

    steps = 0
    while True:
        arr[0] += 1
        arr[1] += 1
        arr[2] -= 1
        steps += 1
        arr.sort()

        if arr[0] == arr[1] == arr[2]:
            return steps
        
        # If the values are stuck and can't be made equal
        if (arr[0] == arr[1] and arr[1] + 1 == arr[2]) or (arr[1] == arr[2] and arr[0] + 1 == arr[1]):
            return -1

# Input handling
T = int(input())  # Number of test cases
for _ in range(T):
    # Read the triplet values for each test case
    user_input = input()  # Take input for triplet
    print(f"Input received: {user_input}")  # Debugging: print what we received
    a, b, c = map(int, user_input.split())  # Split the input and convert to integers
    print(min_steps_to_equal(a, b, c))  # Print the result of the function