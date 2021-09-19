# https://leetcode.com/problems/last-stone-weight/

"""
Solved without heapq
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max_y = stones.pop(stones.index(max(stones)))
            max_x = stones.pop(stones.index(max(stones)))
            if max_y > max_x:
                stones.append(max_y - max_x)
            elif max_y < max_x:
                stones.append(max_x - max_y)
        
        if stones:
            return (stones[0])
        return 0
                
"""
Runtime: 32 ms, faster than 67.85% of Python3 online submissions for Last Stone Weight.
Memory Usage: 14.4 MB, less than 19.45% of Python3 online submissions for Last Stone Weight.
"""          

