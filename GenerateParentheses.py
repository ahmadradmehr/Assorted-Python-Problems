"""
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class GenerateParentheses:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generate(res, "", n, n)
        return res

    def generate(self, res, s, n_open, n_close):
        if not n_open and not n_close:
            res.append(s)
        if n_open < n_close:
            self.generate(res, s + ')', n_open, n_close - 1)
        if n_open:
            self.generate(res, s + '(', n_open - 1, n_close)
