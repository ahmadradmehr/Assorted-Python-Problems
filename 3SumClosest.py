"""
3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""


class ThreeSumClosest:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if abs(current - target) < abs(closest - target):
                    closest = current
                if current < target:
                    j += 1
                elif current > target:
                    k -= 1
                else:
                    return target
        return closest
