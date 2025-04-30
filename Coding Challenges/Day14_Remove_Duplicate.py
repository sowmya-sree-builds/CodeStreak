# 🧠 Problem: Remove Duplicate Elements from an Array
# Given an array of integers, remove all duplicates while preserving the original order.

from typing import List

def remove_duplicates(arr: List[int]) -> List[int]:
    seen = set()
    unique = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            unique.append(num)
    return unique

def main():
    arr = [1, 2, 2, 3, 88, 4, 4, 5, 6, 7]
    print("Unique elements are:", remove_duplicates(arr))

if __name__ == "__main__":
    main()
