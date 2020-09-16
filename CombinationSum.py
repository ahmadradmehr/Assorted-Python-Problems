"""
*** Combination Sum ***


Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
"""


class CombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.createCombination(candidates, target, res, [], 0)
        return res

    def createCombination(self, candidates, target, res, curr, pos):
        if target == 0:
            res.append(curr)
            return
        for i in range(pos, len(candidates)):
            if target - candidates[i] < 0:
                break
            self.createCombination(candidates, target - candidates[i], res, curr + [candidates[i]], i)
