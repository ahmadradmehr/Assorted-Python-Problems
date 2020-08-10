"""
ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class ZigZagConversion:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = r = 0
        d = "down"
        vec = [""] * numRows
        while r < len(s):
            if d == "down":
                vec[n] += s[r]
                if n == numRows-1:
                    n -= 1
                    d = "up"
                else:
                    n += 1
            elif d == "up":
                vec[n] += s[r]
                if n == 0:
                    n += 1
                    d = "down"
                else:
                    n -= 1
            r += 1
        res = ""
        for v in vec:
            res += v
        return res