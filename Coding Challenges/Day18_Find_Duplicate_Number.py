# Day18_Find_Duplicate_Number.py
"""
Problem: Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n,
return the duplicate number using constant space and less than O(n^2) time.
"""

class Solution:
    def findDuplicate(self, nums):
        # Phase 1: Detect intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find entrance to cycle (duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
    print(sol.findDuplicate([3, 1, 3, 4, 2]))  # Output: 3
