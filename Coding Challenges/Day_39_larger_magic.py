 # Day 37: Third Largest Number After Removing Duplicates (No Built-ins)

# Problem:
# Given a list of numbers, remove duplicates manually (without using set or other built-ins)
# and then find the third largest unique number without using sorting or max().

numbers = [7, 3, 9, 3, 5, 9, 2, 7, 8]

# Step 1: Remove duplicates manually
unique = []
for num in numbers:
    found = False
    for u in unique:
        if u == num:
            found = True
            break
    if not found:
        unique.append(num)
        

# Step 2: Find the largest, second largest, and third largest manually
first = second = third = -999999  # placeholder for very small values

for n in unique:
    if n > first:
        third = second
        second = first
        first = n
    elif n > second and n != first:
        third = second
        second = n
    elif n > third and n != second and n != first:
        third = n

if third == -999999:
    print("Not enough unique elements to find third largest")
else:
    print("Third largest unique number is:", third)
