from collections import deque

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        self.stack.append(root)
        

    def next(self) -> int:
        cur = self.stack.pop()
        cur_left = cur.left
        if cur.left:
            cur.left = None
            self.stack.append(cur)
            self.stack.append(cur_left)
            return self.next()
        if cur.right:
            self.stack.append(cur.right)
        return cur.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
