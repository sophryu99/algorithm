class Solution(object):
    def restoreString(self, s, indices):
        
        listShuffle = list(s)
        for x in range(len(s)):
            listShuffle[indices[x]] = s[x]
        return ''.join(listShuffle)