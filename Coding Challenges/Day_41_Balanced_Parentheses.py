# Day 41: Check for Balanced Parentheses using Stack 

def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expression:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return not stack


# 🧩 Test
expr = "{[()()]}"
print("Expression:", expr)
print(" Balanced" if is_balanced(expr) else " Not Balanced")

