"""
*** Pow(x, n) ***


Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
"""


class MyPow:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1 or (x == -1 and n % 2 == 1):
            return x
        if (x == -1 and n % 2 == 0) or n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 1:
            return x
        res = self.myPow(x, n//2)
        if n % 2 == 1:
            return res * res * x
        return res * res
