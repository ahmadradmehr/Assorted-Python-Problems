"""
*** Search in Rotated Sorted Array ***


You are given an integer array nums sorted in ascending order, and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
If target is found in the array return its index, otherwise, return -1.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
"""


class SearchInRotatedSortedArray:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[r] > nums[l]:
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] > nums[l]:
                if target > nums[m]:
                    l = m + 1
                elif target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target >= nums[l] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        if nums[r] == target:
            return r
        elif nums[l] == target:
            return l
        return -1
