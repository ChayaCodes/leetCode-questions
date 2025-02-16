# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        cur_less = less_head
        cur_greater = greater_head

        while head:
            if head.val < x:
                cur_less.next = head
                cur_less = cur_less.next
            else:
                cur_greater.next = head
                cur_greater = cur_greater.next 
            head = head.next
        
        cur_greater.next = None
        cur_less.next = greater_head.next
        return less_head.next
        
                