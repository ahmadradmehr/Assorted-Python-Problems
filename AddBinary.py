"""
*** Add Binary ***


Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""


class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        ext = 0
        for i in range(max(len(a), len(b))):
            if i < len(a) and i < len(b):
                n = int(a[-i-1]) + int(b[-i-1]) + ext
            elif i < len(a):
                n = int(a[-i-1]) + ext
            else:
                n = int(b[-i-1]) + ext
            res += str(n % 2)
            ext = n // 2
        if ext:
            res += "1"
        return res[::-1]
