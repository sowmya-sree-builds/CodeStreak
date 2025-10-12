# Day 40: Count Vowels and Consonants using ASCII values.

# Problem:
# Write a program to count vowels and consonants in a string.
# Use ASCII values (ord) instead of direct character matching.
# Ignore digits, spaces, and special characters.

s = "ASCII makes Day 40 fun!"

vowel_ascii = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]  # A,E,I,O,U,a,e,i,o,u
vowel_count = 0
consonant_count = 0

for ch in s:
    ascii_val = ord(ch)

    # Check if it's an alphabet (A-Z or a-z)
    if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
        if ascii_val in vowel_ascii:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
