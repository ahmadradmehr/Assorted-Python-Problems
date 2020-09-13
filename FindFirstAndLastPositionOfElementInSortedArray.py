"""
*** Find First and Last Position of Element in Sorted Array ***


Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
"""


class FindFirstAndLastPosition:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = self.lowerBound(nums, target)
        r = self.lowerBound(nums, target + 1) - 1
        if l < len(nums) and nums[l] == target:
            return [l, r]
        return [-1, -1]

    def lowerBound(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        return l
