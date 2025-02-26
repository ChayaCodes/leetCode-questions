"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root
        
        queue = deque([root])  

        while queue:
            len_level = len(queue)
            prev = None  
            
            for _ in range(len_level):
                cur_node = queue.popleft()  
                
                if prev:
                    prev.next = cur_node  
                
                prev = cur_node

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

        return root
        
        