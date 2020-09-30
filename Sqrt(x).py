"""
*** Sqrt(x) ***


Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


class MySqrt:
    def mySqrt(self, x: int) -> int:
        a = 0
        b = x
        d = b - a
        while d > 1:
            m = (a + b) // 2
            if m ** 2 < x:
                a = m
            else:
                b = m
            d = b - a
        if b ** 2 <= x:
            return b
        return a
