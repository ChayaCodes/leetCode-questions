from collections import deque

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        self.append_leftmost_branch(root)

    def next(self) -> int:
        current = self.stack.pop()
        if current.right:
            self.append_leftmost_branch(current.right)
        return current.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def append_leftmost_branch(self, root: Optional[TreeNode]):
        while root:
            self.stack.append(root)
            root = root.left
