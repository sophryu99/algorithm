# https://leetcode.com/problems/max-consecutive-ones-iii/

# Find contiguous array which consists of k 0's and maximum 1's

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            k -= 1 - nums[right]
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1
        return right - left + 1

"""
Runtime: 568 ms, faster than 89.37% of Python3 online submissions for Max Consecutive Ones III.
Memory Usage: 14.9 MB, less than 36.17% of Python3 online submissions for Max Consecutive Ones III.
"""