# Day 46: Reverse a String using Stack 
def reverse_string(s):
    stack = []
    for ch in s:
        stack.append(ch)
    res = ""
    while stack:
        res += stack.pop()
    return res

print(reverse_string("CodeStreak"))
