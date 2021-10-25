# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "aabcbbcbb"
        # "abcbbcbb"
        # "cbbcbb"
        """
        left = 0, right = 1, s[0: 2] = [a, a], set(s[0:2]) = (a)
        s = s[1: 2] = [a, b, c, a, b, c, b, b], left = 0, right = 1
        left = 0, right = 1 s[0: 2] = [a, b], set(s[0:2]) = True
        locallen = 2, maxlen = 2, right = 2
        left = 0, right = 2, s[0: 3] = [a, b, c], set s[] = True
        locallen = 3, maxlen = 3, right = 4
        left = 0, right = 3, s[0: 4] = [a, b, c, b], set s[] = False
        new = s[3] = b, cut = 1, s = [2:], left = 0, right = 1
        "cbbcbb"
        left = 0, right = 1, s[0: 2] = [c, b] == set() == True
        locallen = 2, right 2
        left = 0, right = 2 s[0: 3] = [c, b, b] == set() == False
        new = s[2] = b, cut = s[0: 2].index(b) = 1, s = s[2:] = "bcbb"
        
        """
        if len(s) == 0:
            return 0
        
        maxlen = 1
        locallen = 1
        left = 0
        right = 1
        check = [s[left]]
        s = list(s)
        
        
        while right < len(s):
            if len(s[left: right + 1]) == len(set(s[left: right + 1])):
                locallen += 1
                if locallen > maxlen:
                    maxlen = locallen
                right += 1
            else:
                new = s[right]
                cut = s[left: right].index(new)
                s = s[cut + 1:]
                left, right = 0, 1
                locallen = 1
                
        return maxlen

"""
Runtime: 6922 ms, faster than 5.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.6 MB, less than 6.56% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""

# Better Solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "aabcbbcbb"
        # "abcbbcbb"
        # "cbbcbb"
        """
        left = 0, right = 1, s[0: 2] = [a, a], set(s[0:2]) = (a)
        s = s[1: 2] = [a, b, c, a, b, c, b, b], left = 0, right = 1
        left = 0, right = 1 s[0: 2] = [a, b], set(s[0:2]) = True
        locallen = 2, maxlen = 2, right = 2
        left = 0, right = 2, s[0: 3] = [a, b, c], set s[] = True
        locallen = 3, maxlen = 3, right = 4
        left = 0, right = 3, s[0: 4] = [a, b, c, b], set s[] = False
        new = s[3] = b, cut = 1, s = [2:], left = 0, right = 1
        "cbbcbb"
        left = 0, right = 1, s[0: 2] = [c, b] == set() == True
        locallen = 2, right 2
        left = 0, right = 2 s[0: 3] = [c, b, b] == set() == False
        new = s[2] = b, cut = s[0: 2].index(b) = 1, s = s[2:] = "bcbb"
        
        """
        if len(s) == 0:
            return 0
        if s.isspace():
            return 1
        max_size = float('-inf')
        start = 0 #start of our sliding window
        curr_string = "" #our current string
        keep_track = []

        for end, char in enumerate(s):
            curr_string += char
            while char in keep_track:
                curr_string = s[start:end]
                max_size = max(max_size, len(curr_string))
                start += 1
                keep_track = keep_track[1:]

            keep_track.append(char)
            max_size = max(max_size, len(curr_string))
        return max_size
        
### 3rd try

"""
1. Iterate through the string with start and end index.
2. Append the unique lettes until a recurring letter occurs.
3. Compare the length of the string slice and reset the max length. 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
            
        start = 0
        end = 1
        d = [s[start]]
        maxlen = len(d)
        
        while end < len(s):
            if s[end] in d:
                idx = d.index(s[end])
                d = d[idx + 1:]
                start = idx + 1
                d.append(s[end])
                end +=1
                if len(d) > maxlen:
                    maxlen = len(d)
                
            else:
                d.append(s[end])
                end += 1
                if len(d) > maxlen:
                    maxlen = len(d)
                        
        return maxlen
    
"""
Runtime: 80 ms, faster than 51.72% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.3 MB, less than 54.36% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""