# https://leetcode.com/problems/sliding-window-maximum/

import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize a deque
        windowQueue = collections.deque()
        maxSlide = []
        for i in range(len(nums)):
            if windowQueue and windowQueue[0] == (i-k):
                windowQueue.popleft()
            # While windowQueue exists
            while windowQueue and nums[i] > nums[windowQueue[-1]]:
                # Remove the leftmost element of windowQueue
                windowQueue.pop()
            windowQueue.append(i)
            
            # If i >= k - 1, append the first element of windowQueue to maxSlide
            if i >= k-1:
                maxSlide.append(nums[windowQueue[0]])

        return maxSlide

"""
Runtime: 1716 ms, faster than 80.43% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 30.8 MB, less than 14.91% of Python3 online submissions for Sliding Window Maximum.
"""