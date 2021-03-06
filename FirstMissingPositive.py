"""
41. First Missing Positive


Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
Follow up:
Your algorithm should run in O(n) time and uses constant extra space.
"""


class FirstMissingPositive:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                temp = nums[i]-1
                nums[i], nums[temp] = nums[temp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1
