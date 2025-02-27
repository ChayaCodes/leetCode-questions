from collections import deque


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        self._push_left_branch(root)

    def _push_left_branch(self, node: Optional[TreeNode]):
        """ פונקציה עזר שמוסיפה את כל תת-העץ השמאלי למחסנית """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """ מחזירה את הערך הבא בסדר ה- Inorder """
        if not self.hasNext():
            raise Exception("No more elements in BSTIterator")

        cur = self.stack.pop()
        if cur.right:
            self._push_left_branch(cur.right)

        return cur.val

    def hasNext(self) -> bool:
        """ מחזירה האם יש עוד אלמנטים באיטרטור """
        return bool(self.stack)
