# https://leetcode.com/problems/fizz-buzz/
"""
1. For 1 ~ n + 1, check if the index is divisible by certain condition.
2. If the index fulfills the condition, append the value as a string
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append("{}".format(i))
                
        return ans

"""
Runtime: 36 ms, faster than 95.88% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15.1 MB, less than 65.62% of Python3 online submissions for Fizz Buzz.
"""