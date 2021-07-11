# https://leetcode.com/problems/ransom-note/

"""
1. Iterate through ransomeNote, and check if each letters exist in magazine
2. If the letter exists, pop from magazine
3. If not, return False
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.pop(magazine.index(i))
            else:
                return False
                
        return True

"""
Runtime: 104 ms, faster than 12.83% of Python3 online submissions for Ransom Note.
Memory Usage: 14.4 MB, less than 35.32% of Python3 online submissions for Ransom Note.

"""