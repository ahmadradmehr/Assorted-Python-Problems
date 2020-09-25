"""
*** Minimum Path Sum ***


Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class MinimumPathSum:
    def minPathSum(self, grid: List[List[int]]) -> int:
        vec = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    vec[0] = grid[0][0]
                elif i == 0:
                    vec[j] = vec[j-1] + grid[0][j]
                elif j == 0:
                    vec[0] += grid[i][0]
                else:
                    vec[j] = min(vec[j-1], vec[j]) + grid[i][j]
        return vec[-1]
