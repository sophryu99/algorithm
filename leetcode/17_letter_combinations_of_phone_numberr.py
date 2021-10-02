# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

"""
1. Create a dictionary for number-letter information
2. Iterate through the input string to append the according strings to a list
3. Compute all possible combinations of alphabets across the lists
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8' :['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        """
        ['a', 'b', 'c']
        ['d', 'e', 'f']
        ['g', 'h', 'i']
        """
        if digits == "":
            return []
        
        s = []
        for num in digits:
            s.append(d[num])
            
        l = list(itertools.product(*s))
        ans = [''.join(i) for i in l]
        return (ans)

"""
Runtime: 53 ms, faster than 10.03% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.1 MB, less than 85.52% of Python3 online submissions for Letter Combinations of a Phone Number.
"""