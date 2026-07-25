# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        a=ListNode(0,head)
        pre=a
        for _ in range (left-1):
            pre=pre.next
        b=pre.next
        for _ in range(right-left):
            temp=b.next
            b.next=temp.next
            temp.next=pre.next
            pre.next=temp
        return a.next