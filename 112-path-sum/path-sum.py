
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self._hasPathSumRec(root, targetSum)

    def _hasPathSumRec(self, node: Optional[TreeNode], targetSum: int, cur_sum: int = 0) -> bool:
        if not node:
            return False

        cur_sum += node.val
        
        # Check if we are at a leaf node and the current sum matches the target sum
        if not node.left and not node.right:
            return cur_sum == targetSum
        
        # Recursively check the left and right subtrees
        return (self._hasPathSumRec(node.left, targetSum, cur_sum) or 
                self._hasPathSumRec(node.right, targetSum, cur_sum))
