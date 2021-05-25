"""
*** Climbing Stairs ***


You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""


# # Brute Force
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         return self.climb(0, n);

#     def climb(self, i: int, n: int) -> int:
#         if i > n:
#             return 0;
#         if i == n:
#             return 1;
#         return self.climb(i+1, n) + self.climb(i+2, n);

# # Recursion with Memoization
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         mem = [0] * n;
#         return self.climb(0, mem, n);

#     def climb(self, i: int, mem: list, n: int) -> int:
#         if i > n:
#             return 0;
#         if i == n:
#             return 1;
#         if mem[i] > 0:
#             return mem[i];
#         mem[i] = self.climb(i+1, mem, n) + self.climb(i+2, mem, n);
#         return mem[i];

# # Dynamic Programming
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1;
#         dp = [0] * n;
#         dp[0] = 1;
#         dp[1] = 2;
#         for i in range(2, n):
#             dp[i] = dp[i - 1] + dp[i - 2];
#         return dp[n - 1];

# Fibonacci Number
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(2, n):
            third = first + second
            first = second
            second = third
        return second
