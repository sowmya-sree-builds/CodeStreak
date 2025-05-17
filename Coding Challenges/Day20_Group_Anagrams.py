# Day20_Group_Anagrams.py
"""
Problem: Group Anagrams
Group words that are anagrams of each other.
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))  # Create a unique key for each anagram group
            anagram_map[sorted_s].append(s)

        return list(anagram_map.values())  # Return the list of groups

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
