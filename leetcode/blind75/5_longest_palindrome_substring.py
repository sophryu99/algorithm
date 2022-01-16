"""
1. For every elemet in s, try expanding around its center (odd, even separately)
2. Increment right pointer, decrement left pointer if it qualifies a certain condition
3. Re-assign the maximum length of the palindrome and re-assign the starting index
4. Return the string slice from s with the maximum length

Time complexity: O(n**2)
- Expanding a palindrome around its center could take O(n) time

Space complexity: O(1)
- Uses the original string s
"""

class Solution:
    def longestPalindrome(self, s):
        self.maxlen = 0
        self.start = 0
        
        # For every element in s, expand around its center
        for i in range(len(s)):
            # For odd numbered len(s)
            self.expandFromCenter(s,i,i)
            # For even numbered len(s)
            self.expandFromCenter(s,i,i+1)
        return s[self.start:self.start+self.maxlen]
    

    def expandFromCenter(self,s,l,r):
        # While the left and the right index is within the range AND
        # the leftmost and the rightmost elements are the same
        while l > -1 and r < len(s) and s[l] ==s[r]:
            # Increment r, decrement l
            l -= 1
            r += 1
        
        # Reassign the maxlen if the current length is larger than the maxlen
        if self.maxlen < r-l-1:
            self.maxlen = r-l-1
            # Reassign the starting index
            self.start = l + 1
                
                    
                
                
                    
            
       