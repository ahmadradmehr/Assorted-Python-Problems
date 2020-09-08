"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class ValidParentheses:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ']' or c == '}' or c == ')':
                if not stack:
                    return False
                if c == ']' and stack[-1] == '[' or \
                        c == '}' and stack[-1] == '{' or \
                        c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        return False
