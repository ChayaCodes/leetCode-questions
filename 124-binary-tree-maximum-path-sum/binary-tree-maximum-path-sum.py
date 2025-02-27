
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf') 

        def find_max_path(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_max = max(find_max_path(node.left), 0) 
            right_max = max(find_max_path(node.right), 0)

            self.max_sum = max(self.max_sum, left_max + right_max + node.val)

            return node.val + max(left_max, right_max)

        find_max_path(root)
        return self.max_sum
