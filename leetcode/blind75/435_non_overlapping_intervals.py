# https://leetcode.com/problems/non-overlapping-intervals/

"""
The heuristic is: always pick the interval with the earliest end time. Then you can get the maximal number of non-overlapping intervals. (or minimal number to remove).

This is because, the interval with the earliest end time produces the maximal capacity to hold rest intervals.
E.g. Suppose current earliest end time of the rest intervals is x. Then available time slot left for other intervals is [x:]. If we choose another interval with end time y, then available time slot would be [y:]. Since x ≤ y, there is no way [y:] can hold more intervals then [x:]. Thus, the heuristic holds.

Approach: Sort interval by ending time and keep track of current earliest end time. Once next interval's start time is earlier than current end time, then we have to remove one interval. Otherwise, we update earliest end time.

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = float('-inf')
        cnt = 0
        # Sort by the ending time
        intervals.sort(key = lambda x:x[1])
        for s, e in intervals:
            # If the start time is larger than or equal to end, simply pass
            if s >= end:
                # Reset end as current end time
                end = e
            # Else, since this indicates overlap, increment count
            else:
                cnt += 1
                
        return cnt