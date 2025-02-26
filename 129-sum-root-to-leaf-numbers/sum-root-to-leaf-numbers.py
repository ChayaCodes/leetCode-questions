
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self._dfs(root, 0)

    def _is_leaf(self, node: Optional[TreeNode]) -> bool:
        return not node.left and not node.right

    def _calculate_current_sum(self, currentSum: int, value: int) -> int:
        return currentSum * 10 + value

    def _dfs(self, node: Optional[TreeNode], currentSum: int) -> int:
        if not node:
            return 0

        currentSum = self._calculate_current_sum(currentSum, node.val)
        
        if self._is_leaf(node):
            return currentSum
        
        return self._dfs(node.left, currentSum) + self._dfs(node.right, currentSum)
