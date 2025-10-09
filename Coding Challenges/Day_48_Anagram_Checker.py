# Day 48: Check if Two Strings are Anagrams
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
    for val in freq.values():
        if val != 0:
            return False
    return True

print(is_anagram("listen", "silent"))
