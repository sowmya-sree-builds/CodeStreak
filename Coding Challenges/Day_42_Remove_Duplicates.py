# Day 42: Remove Duplicates from List using Set 

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# 🧩 Test
nums = [1, 2, 2, 3, 4, 4, 5]
print("\nOriginal List:", nums)
print("After Removing Duplicates:", remove_duplicates(nums))
