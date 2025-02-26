# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = deque([root])
        
        while stack:
            current_node = stack.pop()
            
            # If there's a right child, push it to the stack first
            if current_node.right:
                stack.append(current_node.right)
            # If there's a left child, push it to the stack
            if current_node.left:
                stack.append(current_node.left)
            
            # Connect the current node to the next node in the flattened structure
            if stack:
                current_node.right = stack[-1]
            current_node.left = None  