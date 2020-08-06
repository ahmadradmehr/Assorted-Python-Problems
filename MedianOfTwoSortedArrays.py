"""
Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
from typing import List


class FindMedianSortedArrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        i = j = last = 0
        while i + j < n / 2:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    last = nums1[i]
                    i += 1
                else:
                    last = nums2[j]
                    j += 1
            elif i < len(nums1):
                last = nums1[i]
                i += 1
            else:
                last = nums2[j]
                j += 1
        if n % 2 == 1:
            return last
        if i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                return (last + nums1[i]) / 2
            else:
                return (last + nums2[j]) / 2
        elif i < len(nums1):
            return (last + nums1[i]) / 2
        else:
            return (last + nums2[j]) / 2
