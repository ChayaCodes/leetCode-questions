
class Solution:
    def _hasPathSumRec(self, node: Optional[TreeNode], targetSum: int, cur_sum: int) -> bool:
        if not node:
            return False

        cur_sum += node.val
        
        if not node.left and not node.right:
            return cur_sum == targetSum
        
        return (self._hasPathSumRec(node.left, targetSum, cur_sum) or 
                self._hasPathSumRec(node.right, targetSum, cur_sum))

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self._hasPathSumRec(root, targetSum, 0)
