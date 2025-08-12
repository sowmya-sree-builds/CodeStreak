# Day 24: Count Vowels, Consonants, Digits & Special Characters
# Difficulty: Easy–Intermediate
# Category: String / TCS / Capgemini Logical

def count_types(s):
    vowels = "aeiouAEIOU"
    v = c = d = sc = 0

    for char in s:
        if char in vowels:
            v += 1
        elif char.isalpha():
            c += 1
        elif char.isdigit():
            d += 1
        else:
            sc += 1

    return v, c, d, sc

# Example test
input_str = "Hello@123#AI"
v, c, d, sc = count_types(input_str)
print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special Characters:", sc)