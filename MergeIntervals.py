"""
*** Merge Intervals ***


Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

Constraints:
intervals[i][0] <= intervals[i][1]
"""


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        i = 0
        while i < len(intervals):
            l = intervals[i][0]
            r = intervals[i][1]
            while i < len(intervals)-1 and intervals[i+1][0] <= r:
                r = max(r, intervals[i+1][1])
                i += 1
            merged.append([l, r])
            i += 1
        return merged
