# Day 47: Find Missing Number in a Sequence (1 to n)
def find_missing(arr, n):
    total = n * (n + 1) // 2
    arr_sum = 0
    for i in arr:
        arr_sum += i
    return total - arr_sum

print(find_missing([1, 2, 4, 5, 6], 6))
