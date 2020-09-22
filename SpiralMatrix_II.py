"""
*** Spiral Matrix II ***


Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class SpiralMatrix_II:
    def generateMatrix(self, n: int) -> List[List[int]]:
        min_i = min_j = 0
        max_i = max_j = n - 1
        spiral = [[0] * n for x in range(n)]
        num = 1
        while num <= n ** 2:
            for j in range(min_j, max_j+1):
                spiral[min_i][j] = num
                num += 1
            min_i += 1
            for i in range(min_i, max_i+1):
                spiral[i][max_j] = num
                num += 1
            max_j -= 1
            for j in range(max_j, min_j-1, -1):
                spiral[max_i][j] = num
                num += 1
            max_i -= 1
            for i in range(max_i, min_i-1, -1):
                spiral[i][min_j] = num
                num += 1
            min_j += 1
        return spiral
