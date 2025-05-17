 # Day3_Maximum_Subarray.py
"""
Problem: Maximum Subarray (Kadane's Algorithm)

Given an integer array nums, find the contiguous subarray with the largest sum.
"""

class Solution:
    def maxSubArray(self, nums):
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

# Test case
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
