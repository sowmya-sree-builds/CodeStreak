# Day12_Substring_with_Maximum_Vowels.py

"""
🧠 Problem:
Given a string 's' and an integer 'k', find the maximum number of vowels
in any substring of length 'k'.

👀 Approach:
We'll use the sliding window technique:
1. Move a window of size 'k' across the string.
2. At each step, count how many vowels are inside the window.
3. Keep track of the maximum count found.

💡 Sliding window helps avoid recounting the whole substring each time.
"""

def max_vowels(s: str, k: int) -> int:
    vowels = set('aeiouAEIOU')  # Include uppercase vowels as well
    max_count = count = 0

    # Initialize the first window
    for i in range(k):
        if s[i] in vowels:
            count += 1
    max_count = count

    # Slide the window across the string
    for i in range(k, len(s)):
        if s[i - k] in vowels:
            count -= 1  # Remove the leftmost character
        if s[i] in vowels:
            count += 1  # Add the new character to the window
        max_count = max(max_count, count)

    return max_count

# 🔎 Example usage:
if __name__ == "__main__":
    print(max_vowels("abciiidef", 3))   # Output: 3
    print(max_vowels("aeiou", 2))       # Output: 2
    print(max_vowels("rhythms", 4))     # Output: 0
