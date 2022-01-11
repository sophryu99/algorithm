# Trees

def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:                                # if no root
            return False                            # return false
        stack = [(root, 0)]                         # stack to store root and sum
        while stack:                            
            root, rsum = stack.pop()                # pop value from stack
            rsum += root.val                        # add root.val to rsum
            if not root.left and not root.right:    # if the tree reaches an end
                if rsum == targetSum:               # if total sum equals target
                    return True                     # return true
            
            if root.right:                          # if right node exists
                stack.append((root.right, rsum))    # redefine root node and rsum
            if root.left:                           # if left node exissts
                stack.append((root.left, rsum))     # redefine root node and rsum
        return False