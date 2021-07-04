# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs, temp = sorted(strs),""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]: temp += strs[0][i]
            else: break
        return temp
            
                
        