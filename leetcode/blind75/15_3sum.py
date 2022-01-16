# https://leetcode.com/problems/3sum/

"""
1. Split nums into three lists: negative numbers, positive numbers, and zeros
2. Create a separate set for negatives and positives for O(1) look-up times
3-1. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
i.e. (-3, 0, 3) = 0
3-2. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
4-1. For all pairs of negative numbers (-3, -1), check to see if their complement (4) exists in the positive number set
4-2. For all pairs of positive numbers (1, 1), check to see if their complement (-2) exists in thenegative number set

Edge case: Have to set the result array as a set to prevent potential duplicates
+ The triplets need to be sorted before adding to the result array to track the duplicates

Time Complexity: O(n*n)
- Have to scan through the array twice to create potential pairs

Space Complexity: O(1)
"""

class Solution(object):
    def threeSum(self, nums):
        # 1
        n, p, z = [], [], []
        res = set()
        
        for num in nums:
            if num < 0:
                n.append(num)
            elif num == 0:
                z.append(num)
            else:
                p.append(num)
                
        # 2
        N, P = set(n), set(p)
        
        # 3-1
        if z:
            for neg in N:
                if abs(neg) in P:
                    res.add((neg, 0, abs(neg)))
                    
        # 3-2
        if 3 <= len(z):
            res.add((0, 0, 0))
            
        # 4-1
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                if abs(n[i] + n[j]) in P:
                    res.add(tuple(sorted([n[i], n[j], abs(n[i] + n[j])])))
        
        # 4-2
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                if -(p[i] + p[j]) in N:
                    res.add(tuple(sorted([-(p[i] + p[j]), p[i], p[j]])))
        
        return res
    
"""
Runtime: 995 ms, faster than 59.09% of Python3 online submissions for 3Sum.
Memory Usage: 18.1 MB, less than 24.00% of Python3 online submissions for 3Sum.
"""
        