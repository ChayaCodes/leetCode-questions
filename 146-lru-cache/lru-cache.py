class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.cache = {}
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def _move_to_end(self, node):
        self._remove(node)
        self._add(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_end(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)