# Day 23: Most Frequent Character in a String
# Difficulty: Easy–Intermediate
# Question Type: TCS / Wipro / Accenture / Campus-level

from collections import Counter

def most_frequent_char(s):
    freq = Counter(s)
    max_freq = max(freq.values())
    max_chars = [char for char, count in freq.items() if count == max_freq]
    return min(max_chars)  # Lexicographically smallest

# Example test
input_string = "betterbeginner"
print("Most Frequent Character:", most_frequent_char(input_string))
