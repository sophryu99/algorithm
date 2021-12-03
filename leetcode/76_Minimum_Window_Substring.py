#  https://leetcode.com/problems/minimum-window-substring/

# Referred to the solution

class Solution:
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        # Dictionary: count of all the unique characters in t.
        dict_t = Counter(t)
        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)
        # left and right pointer
        l, r = 0, 0
        formed = 0
        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]
                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    
            # Keep expanding the window once we are done contracting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

