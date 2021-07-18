# https://leetcode.com/problems/detect-capital/

"""
1. Iterate through word to count uppercase letters
2. If none of the letters are uppercase, return True
3. If the occurence of uppercase letters are equal to the length of the word, return True
4. If the occurence of uppercase letters is one, check if the uppercase is the first element of the string.
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        uppercnt = 0
        
        for i in range(len(word)-1, -1, - 1):
            if word[i].isupper():
                uppercnt +=1
                
        if uppercnt == len(word):
            return True
        elif uppercnt == 1:
            if word[0].isupper():
                return True
            else:
                return False
        elif uppercnt == 0:
            return True
        else:
            return False                

"""
Runtime: 36 ms, faster than 23.27% of Python3 online submissions for Detect Capital.
Memory Usage: 14.3 MB, less than 44.98% of Python3 online submissions for Detect Capital.
"""