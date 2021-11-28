# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sort by the first element of each components
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 2. If the last element of the answer array is less than the first element of the interval element, append the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # 3. If not, merge the current element with the interval element
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

"""
Runtime: 130 ms, faster than 23.55% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.1 MB, less than 84.98% of Python3 online submissions for Merge Intervals.
Retried
"""
        