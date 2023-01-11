### https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Approach
<!-- Describe your approach to solving the problem. -->
**Sliding window**
1. Use a dictionary to store the character as the key, the last appear index has been seen so far as the value
2. Move the pointer when you met a repeated character in your window.

# Complexity
- Time complexity: O(N) -> worst case a full scan of the string
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(M) -> dictionary
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        maxlen = 0
        for r in range(len(s)):
            # If s[r] not in seen, reset the maxlen
            if s[r] not in d:
                maxlen = max(maxlen, r - l + 1)
            # If s[r] in seen, there are two cases:
            # case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
            # case2: s[r] is not inside the current window, we can keep increase the window
            else:
                # If the index of the seen letter is less than left index, update maxlen
                if d[s[r]] < l:
                    maxlen = max(maxlen, r - l + 1)
                else:
                    l = d[s[r]] + 1
            d[s[r]] = r

        return maxlen



```
