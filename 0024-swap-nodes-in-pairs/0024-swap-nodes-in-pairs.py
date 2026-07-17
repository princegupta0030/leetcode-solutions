# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n=ListNode(0)
        n.next=head
        current=n
        while current.next and current.next.next:
            a=current.next
            b=current.next.next

            a.next=b.next
            b.next=a
            current.next=b

            current=a
        return n.next
        