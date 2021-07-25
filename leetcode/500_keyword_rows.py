# https://leetcode.com/problems/keyboard-row/

"""
1. Create a set of alphabets for each row
2. Check if the subset of the input word is in the set of alphabets for each row
3. Append the word if true
"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiopQWERTYUIOP')
        row2 = set('asdfghjklASDFGHJKL')
        row3 = set('zxcvbnmZXCVBNM')
        result = []
        for word in words:
            w = set(list(word))
            if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
                result.append(word)
        return result


"""
Runtime: 24 ms, faster than 94.83% of Python3 online submissions for Keyboard Row.
Memory Usage: 14.2 MB, less than 47.92% of Python3 online submissions for Keyboard Row.
"""