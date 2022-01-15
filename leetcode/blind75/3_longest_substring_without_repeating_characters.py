"""
Sliding window approach but without actually 'creating' the window

1. Iterate through the string and update the key-val as element-index format
2. If the element is already in the dictionary, AND if the current start index is less than or equal to the index of the existing element, reset the start index as dict[currele] + 1
3. If not, set maxLength as max(maxLength, localLength)
currele: a
dict: {'a': 0}
start idx: 0
max length: 1
---
currele: b
dict: {'a': 0, 'b': 1}
start idx: 0
max length: 2
---
currele: c
dict: {'a': 0, 'b': 1, 'c': 2}
start idx: 0
max length: 3
---
currele: a
dict: {'a': 3, 'b': 1, 'c': 2}
start idx: 1
max length: 3
---
currele: b
dict: {'a': 3, 'b': 4, 'c': 2}
start idx: 2
max length: 3
---
currele: c
dict: {'a': 3, 'b': 4, 'c': 5}
start idx: 3
max length: 3
---
currele: b
dict: {'a': 3, 'b': 6, 'c': 5}
start idx: 5
max length: 3
---
currele: b
dict: {'a': 3, 'b': 7, 'c': 5}
start idx: 7
max length: 3
---
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i, ele in enumerate(s):
            # Check if ele is already used
            # And check if the start index is less than or equal to the currele's index
            if ele in usedChar and start <= usedChar[ele]:
                # Reset the start index as the usedChar index + 1
                start = usedChar[ele] + 1
            else:
                # set maxLength as the current length of the string
                maxLength = max(maxLength, i - start + 1)
                
            # Update the latest index of the current string
            usedChar[ele] = i
            # print('currele:', ele)
            # print('dict:', usedChar)
            # print('start idx:', start)
            # print('max length:', maxLength)
            # print('---')
        return maxLength
            
