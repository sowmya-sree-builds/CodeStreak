# 1. Left Triangle Star Pattern
rows = 5
for row in range(1, rows+1):
    print("* " * row)

# 2. Right Triangle Star Pattern
rows = 5
for row in range(1, rows+1):
    print("  " * (rows-row) + "* " * row)

# 3. Inverted Left Triangle Star Pattern
rows = 5
for row in range(rows, 0, -1):
    print("* " * row)

# 4. Inverted Right Triangle Star Pattern
rows = 5
for row in range(rows, 0, -1):
    print("  " * (rows-row) + "* " * row)

# 5. Pyramid Star Pattern
rows = 5
for row in range(1, rows+1):
    print(" " * (rows-row) + "* " * row)

# 6. Inverted Pyramid Star Pattern
rows = 5
for row in range(rows, 0, -1):
    print(" " * (rows-row) + "* " * row)

# 7. Diamond Star Pattern
rows = 5
for row in range(1, rows+1):
    print(" " * (rows-row) + "* " * row)
for row in range(rows-1, 0, -1):
    print(" " * (rows-row) + "* " * row)

# 8. Hollow Diamond Star Pattern
rows = 5
for row in range(1, rows+1):
    print(" "*(rows-row) + "*" + " "*(2*row-3) + ("*" if row>1 else ""))
for row in range(rows-1, 0, -1):
    print(" "*(rows-row) + "*" + " "*(2*row-3) + ("*" if row>1 else ""))

# 9. Left Triangle Number Pattern
rows = 5
for row in range(1, rows+1):
    for col in range(1, row+1):
        print(col, end=" ")
    print()

# 10. Right Triangle Number Pattern
rows = 5
for row in range(1, rows+1):
    print(" " * (rows-row), end="")
    for col in range(1, row+1):
        print(col, end=" ")
    print()

# 11. Inverted Left Triangle Numbers
rows = 5
for row in range(rows, 0, -1):
    for col in range(1, row+1):
        print(col, end=" ")
    print()

# 12. Inverted Right Triangle Numbers
rows = 5
for row in range(rows, 0, -1):
    print(" " * (rows-row), end="")
    for col in range(1, row+1):
        print(col, end=" ")
    print()

# 13. Odd Numbers Triangle
rows = 5
num = 1
for row in range(1, rows+1):
    for col in range(row):
        print(num, end=" ")
        num += 2
    print()

# 14. Pyramid of Numbers
rows = 5
for row in range(1, rows+1):
    print(" " * (rows-row), end="")
    for col in range(1, row+1):
        print(col, end="")
    for col in range(row-1, 0, -1):
        print(col, end="")
    print()

# 15. Pascal’s Triangle
from math import comb
rows = 5
for row in range(rows):
    print(" "*(rows-row), end="")
    for col in range(row+1):
        print(comb(row, col), end=" ")
    print()

# 16. Hollow Pyramid Star Pattern
rows = 5
for row in range(1, rows+1):
    for col in range(1, rows-row+1):
        print(" ", end="")
    for col in range(1, 2*row):
        if col==1 or col==2*row-1 or row==rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 17. Diamond Number Pattern
rows = 5
for row in range(1, rows+1):
    print(" "*(rows-row), end="")
    for col in range(1, row+1):
        print(col, end="")
    for col in range(row-1, 0, -1):
        print(col, end="")
    print()
for row in range(rows-1, 0, -1):
    print(" "*(rows-row), end="")
    for col in range(1, row+1):
        print(col, end="")
    for col in range(row-1, 0, -1):
        print(col, end="")
    print()

# 18. Solid Square of Stars
rows = 5
for row in range(rows):
    print("* " * rows)

# 19. Hollow Square of Stars
rows = 5
for row in range(rows):
    for col in range(rows):
        if row==0 or row==rows-1 or col==0 or col==rows-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 20. Double Triangle Star Pattern (hourglass style)
rows = 5
for row in range(1, rows+1):
    print("* " * row)
for row in range(rows-1, 0, -1):
    print("* " * row)
