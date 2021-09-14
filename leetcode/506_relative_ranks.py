# https://leetcode.com/problems/relative-ranks/

"""
1. Sort the score list in a descending order
2. Replace values of top three scores with the string values
3. Iterate through the rest of the list and number the results
"""

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse = True)
        for i in range(len(score)):
            if i == 0:
                score[score.index(sorted_score[0])] = 'Gold Medal'
            elif i == 1:
                score[score.index(sorted_score[1])] = 'Silver Medal'
            elif i == 2:
                score[score.index(sorted_score[2])] = 'Bronze Medal'
            else:
                score[score.index(sorted_score[i])] = str(i + 1)
            
        return score
        
"""
Runtime: 728 ms, faster than 7.38% of Python3 online submissions for Relative Ranks.
Memory Usage: 14.8 MB, less than 99.04% of Python3 online submissions for Relative Ranks.
"""