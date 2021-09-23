# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        """
        num = 5
        bin(num) = 101
        [1, 0, 1]
        Iterate through the list, and switch every elements to the other number
        [0, 1, 0]
        num = 010
        """
        bin_num = format(num, "b")
        bin_num_lst = list(bin_num) # ['1', '0', '1']
        
        for i in range(len(bin_num_lst)):
            if bin_num_lst[i] == '0':
                bin_num_lst[i] = '1'
            else:
                bin_num_lst[i] = '0'
                
        num_bin = ''.join(bin_num_lst)
                
        return int(num_bin, 2)

"""
Big O Analysis
- 
"""
"""
Runtime: 28 ms, faster than 84.15% of Python3 online submissions for Number Complement.
Memory Usage: 14.2 MB, less than 68.81% of Python3 online submissions for Number Complement.
"""