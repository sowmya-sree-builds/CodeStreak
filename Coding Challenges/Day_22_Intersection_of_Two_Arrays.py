# Day 22: Intersection of Two Arrays
# Problem Link: https://leetcode.com/problems/intersection-of-two-arrays/
# Difficulty: Easy

"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique, and you may return the result in any order.
"""

def intersection(nums1, nums2):
    # Convert both arrays to sets to remove duplicates
    set1 = set(nums1)
    set2 = set(nums2)

    # Intersection of two sets gives the common unique elements
    result = list(set1 & set2)
    
    return result


# 🔎 Example usage:
if __name__ == "__main__":
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print("Intersection:", intersection(nums1, nums2))  # Output: [9, 4] or [4, 9]
