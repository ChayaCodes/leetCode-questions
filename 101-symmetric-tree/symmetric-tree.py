# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def is_mirror(left, right):
            if not left or not right:
                return left == right
            return left.val == right.val and is_mirror(left.right, right.left) and is_mirror(left.left, right.right)
        return is_mirror(root.left, root.right)