"""
Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class ReverseInteger:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        if x < 0 and rev.bit_length() < 32:
            return -rev
        elif x > 0 and rev.bit_length() < 32:
            return rev
        return 0
