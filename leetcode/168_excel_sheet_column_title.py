class Solution:
    # @return a string
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)

"""
Runtime: 45 ms, faster than 45.51% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 13.9 MB, less than 26.63% of Python3 online submissions for Excel Sheet Column Title.
"""