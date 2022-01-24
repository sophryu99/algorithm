# https://leetcode.com/problems/longest-repeating-character-replacement/

"""
We use a window ranging from index start to end
We only look in characters inside this window and keep track of their counts
We can allow up to K chars that are not the most frequent char in our window

Shift the right index of the window if current_window_size - most_occurence_of_an_ele > k.
current_window_size - most_occurence_of_an_ele indicates the number of characters that need to be changed.

"AABABBA", k = 1
A
AA
AAB
AABA
AABAB -> Ran out of k capacity to replace, shrink window, reset max_window_size
ABAB -> Ran out of k capacity to replace, shrink window, reset max_window_size
BAB
BABB
BABBA -> Ran out of k capacity to replace, shrink window, reset max_window_size
ABBA

max_window_size = 4

######################################################################
Code writeup:
s = "AABABBA", k = 1
max_window = 0
start = 0

""
end = 0, ele = 'A'
window_counts = {'A': 1}
len(current_window) - most_occured_letter_count = 0
max_window = 1

"A"
end = 1, ele = 'A'
window_counts = {'A': 2}
len(current_window) - most_occured_letter_count = 0
max_window = 2

"AA"
end = 2, ele = 'B'
window_counts = {'A': 2, 'B': 1}
len(current_window) - most_occured_letter_count = 1
max_window = 3

"AAB"
end = 3, ele = 'A'
window_counts = {'A': 3, 'B': 1}
len(current_window) - most_occured_letter_count = 1
max_window = 4

"AABA"
end = 4, ele = 'B'
window_counts = {'A': 3, 'B': 2}
len(current_window) - most_occured_letter_count = 2
window_counts = {'A': 2, 'B': 2}
start = 1
max_window = 4

"ABAB"
end = 5, ele = 'B'
window_counts = {'A': 3, 'B': 2}
len(current_window) - most_occured_letter_count = 2
window_counts = {'A': 2, 'B': 2}
start = 1
max_window = 4

...
"""
from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k):  
        max_window = 0
        window_counts = defaultdict(int)
        start = 0 
        for end, ele in enumerate(s):
            # Increment the count of current letter
            window_counts[ele] += 1
            # Size of the current window - most_occured_letter_count
            while end - start + 1 - max(window_counts.values()) > k:
                window_counts[s[start]] -=1
                start += 1
            # Reset max_window as larger length window
            max_window = max(max_window, end - start + 1)
        return max_window
        
"""
Runtime: 218 ms, faster than 29.19% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 14.3 MB, less than 80.17% of Python3 online submissions for Longest Repeating Character Replacement.
"""