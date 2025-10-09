# Day 50: Count Frequency of Each Element (without collections)
def count_frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for key in freq:
        print(f"{key} occurs {freq[key]} times")

count_frequency([1, 2, 2, 3, 3, 3, 4, 4])
