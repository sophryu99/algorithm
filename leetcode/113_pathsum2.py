# https://leetcode.com/problems/path-sum-ii/

class Solution:
        
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        return self._pathSum(root, targetSum, [], [])
        
    def _pathSum(self, root, targetSum, path, result):
         if root is None:
            return result

         if targetSum == root.val and root.left is None and root.right is None:
            return result + [path + [root.val]]
        
         else:
            return self._pathSum(root.left, targetSum - root.val, path + [root.val], result) + self._pathSum(root.right, targetSum - root.val, path + [root.val], result)
        