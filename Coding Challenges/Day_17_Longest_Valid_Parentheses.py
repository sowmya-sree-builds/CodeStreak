# day17_longest_valid_parentheses.py
"""
Problem: Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length 
of the longest valid (well-formed) parentheses substring.

Examples:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 3 * 10^4
s[i] is '(' or ')'
"""

class Solution:
    def longestValidParentheses(self, S: str) -> int:
        stack, ans = [-1], 0
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
            elif len(stack) == 1:
                stack[0] = i
            else:
                stack.pop()
                ans = max(ans, i - stack[-1])
        return ans

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestValidParentheses("(()"))       # Output: 2
    print(sol.longestValidParentheses(")()())"))    # Output: 4
    print(sol.longestValidParentheses(""))          # Output: 0
