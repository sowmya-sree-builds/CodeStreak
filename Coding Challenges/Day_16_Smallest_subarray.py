
"""
Problem: Given a number x and an array of integers arr,
find the smallest subarray with sum greater than x.
Return 0 if no such subarray exists.

Examples:
Input: x = 51, arr = [1, 4, 45, 6, 0, 19]
Output: 3
Explanation: Minimum length subarray is [4, 45, 6]

Input: x = 100, arr = [1, 10, 5, 2, 7]
Output: 0
Explanation: No subarray exists

Constraints:
1 ≤ arr.size, x ≤ 10^5
0 ≤ arr[i] ≤ 10^4
"""

def smallest_subarray_with_sum(x, arr):
    n = len(arr)
    min_len = n + 1
    curr_sum = 0
    start = 0

    for end in range(n):
        curr_sum += arr[end]

        while curr_sum > x:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    return min_len if min_len != n + 1 else 0

# Test cases
print(smallest_subarray_with_sum(51, [1, 4, 45, 6, 0, 19]))  # Output: 3
print(smallest_subarray_with_sum(100, [1, 10, 5, 2, 7]))     # Output: 0
