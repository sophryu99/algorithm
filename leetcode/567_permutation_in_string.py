# https://leetcode.com/problems/permutation-in-string/

# Sliding window approach
# 1. Check if the count of the window is equal to the count of s1. 
# 2. Check if the count of a string is the list of: [the number of a's it has, the number of b's,... , the number of z's.]
# 3. Maintain the window by deleting the value of s2[i - len(s1)] when it gets larger than len(s1). 
# 4. Check if it is equal to the target. 


class Solution:
    def checkInclusion(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False

