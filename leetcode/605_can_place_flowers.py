"""
Approach:
1. Search for conditions where a flower can be planted
- When the first index is 0, and the next is 0
- When the index i-1, i+1, and i is 0.
- When the last index is 0, and before is 0
2. If the index is available for placing flower, replace the index with 1.
3. Continue searching

Exceptions to handle:
1. When the flowerbed length is 1
2. When n is 0

"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if n == 0:                                                  # when no flowers are planted
            return True
    
        if len(flowerbed) == 1 and flowerbed[0] == 0:               # when flowerbed length is 0
            return True
        elif len(flowerbed) == 1 and flowerbed[0] == 1:
            return False
          
        for i in range(len(flowerbed)):
            if i == 0:                                              # for the first index of the flowerbed
                if flowerbed[0] == 0 and flowerbed[1] == 0:
                    count += 1                                      # increment count
                    flowerbed[0] = 1                                # mark as planted
           
            elif (i > 0 and i < len(flowerbed)-1):                  # for mid indexes of the flowerbed
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    count += 1                                      # increment count
                    flowerbed[i] = 1                                # mark as planted
            else:                                                   # for the last index of the flowerbed
                if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                    count += 1                                      # increment count
                    flowerbed[-1] = 1                               # mark as counted
        
        if count >= n:                                              # if count is availble for n flowers
            return True
        else:
            return False
        
"""
Runtime: 180 ms, faster than 26.97% of Python3 online submissions for Can Place Flowers.
Memory Usage: 14.6 MB, less than 38.25% of Python3 online submissions for Can Place Flowers.
"""          
