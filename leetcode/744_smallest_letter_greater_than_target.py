# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

"""
Approach:
1. Convert the alphabet into numerical values => ord(num) - 96
2. If the target is BEFORE the alphabets in the letters list, calculate the difference and return the minimum difference.
3. If the target is AFTER the alphabets in the letters list, calculate the difference and return the maximum difference.
4. Store each values in diff_min, diff_max arrays, and return the letter for the min, max values accordingly.


"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        tar = ord(target) - 96                                          # convert target alphabet to numerical value
        diff_min = []                                                   # array for target BEFORE the letters array
        diff_max = []                                                   # array for target AFTER the letters array
        letter = ""                                                     # save the letter for the min, max diff vals
        for i in range(len(letters)):
            if ((ord(letters[i]) - 96) > tar):                          # for target BEFORE
                diff_min.append(abs((ord(letters[i]) - 96) - tar))      # append the difference to diff_min arr
                if min(diff_min) == abs((ord(letters[i]) - 96) - tar):
                    letter = letters[i]                                 # if it is min val, equate letter
                    
            else:                                                       # for target AFTER
                diff_max.append(abs((ord(letters[i]) - 96) - tar))      # append the difference to diff_max arr
                if max(diff_max) == abs((ord(letters[i]) - 96) - tar):  
                    letter = letters[i]                                 # if it is max val, equate letter
                
        return letter
                

"""
Runtime: 2068 ms, faster than 5.13% of Python3 online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 14.8 MB, less than 8.70% of Python3 online submissions for Find Smallest Letter Greater Than Target.

Should try to find more efficient approach: reduce runtime
"""
            
        
        
