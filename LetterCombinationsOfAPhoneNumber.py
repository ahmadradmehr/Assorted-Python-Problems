"""
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class LetterCombinations:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        m = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res = []
        pos = len(digits) * [0]
        n = len(digits) - 1
        while n >= 0:
            s = ""
            for i in range(len(digits)):
                s += m[digits[i]][pos[i]]
            res.append(s)
            n = len(digits) - 1
            pos[n] += 1
            while n >= 0 and pos[n] == len(m[digits[n]]):
                pos[n] = 0
                n -= 1
                pos[n] += 1
        return res
