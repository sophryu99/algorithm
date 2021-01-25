# https://leetcode.com/problems/pascals-triangle/

"""
Approach:
1. Create list of 1s for the first two rows and save it to the final array
2. From the third rows, call the previous row and calculate sums of each elements
3. Initialize new list with the first and last element as 1, and fill in the middle values as the sums 
4. Save the new list to the final array
5. Repeat for numRows
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = []
        for i in range(numRows):     
            lst = [1] * (i+1)                                   # create list of 1s for the first two rows                 
            if (i+1) > 2:                                       # from the third rows
                for j in range(len(final[-1])-1):
                    new = final[-1][j] + final[-1][j+1]         # calculate the sum from the previous row
                    lst[0] = 1                                  # initialize new list
                    lst[-1] = 1
                    lst[j+1] = new
            final.append(lst)                                   # append when done
        
        return final

"""
Runtime: 32 ms, faster than 62.83% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14.3 MB, less than 59.59% of Python3 online submissions for Pascal's Triangle.
"""
