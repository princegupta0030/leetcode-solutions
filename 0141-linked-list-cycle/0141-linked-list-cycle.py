# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a=head
        z=head
        while z and z.next:
            a=a.next
            z=z.next.next
            if a==z:
                return True
        return False