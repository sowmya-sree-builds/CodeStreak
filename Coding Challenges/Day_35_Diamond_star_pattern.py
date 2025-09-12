# Day 35: Diamond Star Pattern

rows = 5

# Upper half (pyramid)
for row in range(1, rows + 1):
    # print spaces
    for space in range(rows - row):
        print(" ", end="")
    # print stars
    for star in range(row):
        print("* ", end="")
    print()

# Lower half (inverted pyramid)
for row in range(rows - 1, 0, -1):
    # print spaces
    for space in range(rows - row):
        print(" ", end="")
    # print stars
    for star in range(row):
        print("* ", end="")
    print()
