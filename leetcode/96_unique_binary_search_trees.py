# https://leetcode.com/problems/unique-binary-search-trees/

"""
Condition of Binary Search Tree:

- If a node is a left child, then its key and the keys of the nodes in its right subtree are less than its parent's key.
- If a node is a right child, then its key and the keys of the nodes in its left subtree are greater than its parent's key.
root = 1

dp[n] := the number of structurally unique BST's which has n nodes with val 1~n
dp[n] = helper(n)

Form 1~n nodes
If we use 1 as root, the left subtree possible count will be dp[1-1] and right subtree be dp[n-1], the count will be dp[0]*dp[n-1].
If we use 2 as root, the left subtree possible count will be dp[2-1] and right subtree be dp[n-2], the count will be dp[1]*dp[n-2].
If we use 3 as root, the left subtree possible count will be dp[3-1] and right subtree be dp[n-3], the count will be dp[2]*dp[n-3].
...
If we use i as root, the left subtree possible count will be dp[i-1] and right subtree be dp[n-i], the count will be dp[i-1]*dp[n-i].

So the number of structurally unique BST's which has n nodes with val 1~n, will be the sum above.

Time: O(N ** 2)
"""

class Solution: 
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
            
        for i in range(2, n + 1):
            total = 2 * dp[i-1] # 2 * current num
            for j in range(2, i):
                total += dp[j-1] * dp[i-j]
            dp[i] = total
        return dp[n]
        
"""
Runtime: 32 ms, faster than 65.39% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 14.4 MB, less than 14.57% of Python3 online submissions for Unique Binary Search Trees.
"""
            
        