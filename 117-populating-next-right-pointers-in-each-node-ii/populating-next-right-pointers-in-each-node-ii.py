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
            return None
        
        queue = deque([root])  

        while queue:
            level_size = len(queue)  
            
            for i in range(level_size):
                current_node = queue.popleft() 
                
                if i < level_size - 1:
                    current_node.next = queue[0] 

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return root
        