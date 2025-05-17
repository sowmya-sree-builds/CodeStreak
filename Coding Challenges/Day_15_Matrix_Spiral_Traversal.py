"""🧠 Day15: Matrix Spiral Traversal

Given a 2D matrix of size R x C, print all elements of the matrix in a spiral order starting from the top-left corner.

📥 Input:
- First line contains two integers R and C (number of rows and columns).
- Next R lines contain C integers each, representing the matrix.

📤 Output:
- A single list of elements in spiral order.

🔍 Example:
Input:
3 3
1 2 3
4 5 6
7 8 9

Output:
[1, 2, 3, 6, 9, 8, 7, 4, 5]

"""

def spiral_traversal(matrix):
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    while top < bottom and left < right:
        # Traverse Left to Right
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1

        # Traverse Top to Bottom
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1

        if not (top < bottom and left < right):
            break

        # Traverse Right to Left
        for i in range(right - 1, left - 1, -1):
            result.append(matrix[bottom - 1][i])
        bottom -= 1

        # Traverse Bottom to Top
        for i in range(bottom - 1, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

    return result

def main():
    R, C = map(int, input("Enter number of rows and columns: ").split())
    print("Enter the matrix row by row:")
    matrix = [list(map(int, input().split())) for _ in range(R)]
    print("Spiral Order:", spiral_traversal(matrix))

if __name__ == "__main__":
    main()
