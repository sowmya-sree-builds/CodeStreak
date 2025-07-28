# Day 21: First Unique Character in a String
# Problem:
# Given a string s, find the first non-repeating character in it 
# and return its index. If it does not exist, return -1.

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count the frequency of each character in the string
        count = Counter(s)

        # Step 2: Loop through the string to find the first unique character
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i  # Return the index of the first non-repeating character

        return -1  # If there is no unique character

# Example usage:
if __name__ == "__main__":
    s = "leetcode"
    sol = Solution()
    print("Index of first unique character:", sol.firstUniqChar(s))
