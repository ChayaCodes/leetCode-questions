class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def build_tree_rec(start, end):
            if start >= end:
                return None

            node_val = preorder[self.preorder_index]
            node = TreeNode(node_val)
            self.preorder_index += 1
            
            inorder_index = inorder_map[node_val]
            
            node.left = build_tree_rec(start, inorder_index)
            node.right = build_tree_rec(inorder_index + 1, end)
            
            return node

        self.preorder_index = 0
        inorder_map = {val: idx for idx, val in enumerate(inorder)}  
        return build_tree_rec(0, len(preorder))