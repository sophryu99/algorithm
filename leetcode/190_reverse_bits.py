# https://leetcode.com/problems/reverse-bits/

def reverseBits(self, n):
    ans = 0
    for i in xrange(32):
        ans = (ans << 1) + (n & 1)
        n >>= 1
    return ans
