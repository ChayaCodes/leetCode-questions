class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left or not right:
                return left == right
            return left.val == right.val and is_mirror(left.right, right.left) and is_mirror(left.left, right.right)
        
        if not root:
            return True
        return is_mirror(root.left, root.right)