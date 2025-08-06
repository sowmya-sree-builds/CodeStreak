"""
🔍 Problem Statement:
Given a string S, find:

1. The first non-repeating character (or "None" if none exists).
2. The most frequent character (or the first character if all are unique).

Input1: swadesh
Output1: w s

Input2: aabbcc
Output2: None a
"""

from collections import Counter

def find_characters(S):
    # Count frequency of each character in the string
    freq = Counter(S)

    # Find the first non-repeating character
    non_repeating = None
    for char in S:
        if freq[char] == 1:
            non_repeating = char
            break

    # Find the most frequent character
    most_frequent = max(S, key=lambda x: freq[x])

    # Return the results
    return (non_repeating if non_repeating else "None", most_frequent)

# Input
T = int(input())  # Number of test cases

for _ in range(T):
    S = input().strip()  # Input string
    
    non_repeating, most_frequent = find_characters(S)
    
    print(non_repeating, most_frequent)  # Print results
