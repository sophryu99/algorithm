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
        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort according to the 0th element of the intervals list
        s = sorted(intervals)
        ans = [s[0]]
        curr = 1
        while curr < len(s):
            # If the second element of the list s is larger than the next element's first index
            if ans[-1][1] >= s[curr][0]:
                # If the second element of the list s is larger than the next element's second index
                if ans[-1][1] < s[curr][1]:
                    # Replace the second element of the list s with the next element's second index
                    ans[-1][1] = s[curr][1]
                # Increment curr index
                curr += 1
            # If the interval doesnt overlap, append the new element
            else:
                ans.append(s[curr])
                curr += 1
        return (ans)
          
"""
Runtime: 84 ms, faster than 78.44% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.1 MB, less than 55.36% of Python3 online submissions for Merge Intervals.
"""