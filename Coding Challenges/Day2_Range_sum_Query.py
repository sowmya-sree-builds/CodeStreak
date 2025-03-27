"""
Problem Statement: Range Sum Query

You are given two integers i and j, where 0 ≤ i < j ≤ 9999.
Your task is to compute the sum of integers from index i to j, inclusive.

Input Format:
- A single integer T representing the number of queries.
- Each of the next T lines contains two integers i and j (0 ≤ i < j ≤ 9999).

Output Format:
- For each query, print a single integer representing the sum of numbers from i to j.

Constraints:
1 ≤ T ≤ 10
0 ≤ i < j ≤ 9999

Example Input:
3
0 3
2 6

Example Output:
6
20
"""

def range_sum(i, j):
    """Returns the sum of numbers from i to j inclusive using arithmetic progression formula"""
    return (j * (j + 1) // 2) - (i * (i + 1) // 2)

# Taking the number of queries
T = int(input("Enter the number of queries: "))

for _ in range(T):
    user_input = input().strip()  # Read input and remove leading/trailing spaces
    values = user_input.split()  # Split into a list of values

    if len(values) < 2:
        print("Invalid input: i & j must be entered as two integers")
        continue

    try:
        i, j = map(int, values)  # Convert inputs to integers

        if not (0 <= i < j <= 9999):
            print("Invalid input: i and j must satisfy 0 ≤ i < j ≤ 9999")
        else:
            print(range_sum(i, j))
    except ValueError:
        print("Invalid input: Please enter two valid integers")
