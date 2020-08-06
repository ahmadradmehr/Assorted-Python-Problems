"""
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class LengthOfLongestSubstring(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        l = r = max_length = 0
        while r < len(s) and l <= len(s)-max_length:
            if s[r] in dic and dic[s[r]] == 1:
                dic[s[l]] -= 1
                l += 1
            else:
                dic[s[r]] = 1
                max_length = max(max_length, r - l + 1)
                r += 1
        return max_length
