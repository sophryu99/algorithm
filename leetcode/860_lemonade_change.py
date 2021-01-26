#https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar = 0
        ten_dollar = 0
        result = True
        
        # if the first order is $10, no change
        if bills[0] == 10:
            result = False
        
        for i in range(len(bills)):
            # if $5, increment five_dollar num
            if bills[i] == 5:
                five_dollar +=1
                result = True
            # if $10, check if five_dollar exists and increment ten_dollar num
            elif bills[i] == 10:
                if five_dollar >= 1:
                    ten_dollar +=1
                    five_dollar -=1
                    result = True
                else:
                    result = False
                    break
            # if $20, check if 1 ten_dollar + 1 five_dollar exists OR 3 five_dollar exists 
            elif bills[i] == 20:
                if ten_dollar >= 1 and five_dollar >= 1:
                    ten_dollar -=1
                    five_dollar -=1
                    result = True
                elif ten_dollar == 0 and five_dollar >= 3:
                    five_dollar -=3
                    result = True
                else:
                    result = False
                    break
                    
        return result
        
"""
Runtime: 140 ms, faster than 63.35% of Python3 online submissions for Lemonade Change.
Memory Usage: 14.7 MB, less than 26.81% of Python3 online submissions for Lemonade Change.
"""
