# Day 43: Find First Non-Repeating Element using Dictionary 

def first_non_repeating(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1

    for item in lst:
        if freq[item] == 1:
            return item
    return None


# 🧩 Test
elements = [9, 4, 9, 6, 7, 4]
print("\nList:", elements)
print("First Non-Repeating Element:", first_non_repeating(elements))

