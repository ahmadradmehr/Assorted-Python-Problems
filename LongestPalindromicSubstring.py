"""
Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class LongestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s) - len(res) / 2:
            temp = self.expandPalindrome(s, i)
            if len(temp) > len(res):
                res = temp
            i += 1
        return res

    def expandPalindrome(self, s, i):
        l = r = i
        while r < len(s) - 1 and s[r + 1] == s[l]:
            r += 1
        while l > 0 and r < len(s) - 1 and s[r + 1] == s[l - 1]:
            r += 1
            l -= 1
        i = r
        return s[l:r + 1]
