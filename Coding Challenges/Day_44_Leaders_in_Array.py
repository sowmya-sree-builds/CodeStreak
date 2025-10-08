# Day 44: Find Leaders in an Array (Right-to-Left Traversal) 

def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    leaders.reverse()
    return leaders


# 🧩 Test
arr = [16, 17, 4, 3, 5, 2]
print("\nArray:", arr)
print("Leaders in Array:", find_leaders(arr))
