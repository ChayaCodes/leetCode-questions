from collections import deque

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque([root]) if root else deque()

    def next(self) -> int:
        cur = self.stack.pop()

        if cur.left:
            self.stack.append(cur)
            self.stack.append(cur.left)
            cur.left = None  # כדי לא לחזור עליו שוב
            return self.next()

        if cur.right:
            self.stack.append(cur.right)

        return cur.val

    def hasNext(self) -> bool:
        return bool(self.stack)
