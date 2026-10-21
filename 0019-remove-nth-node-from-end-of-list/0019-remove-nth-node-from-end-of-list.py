# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        c=0
        temp=head
        while temp is not None:
            c=c+1
            temp=temp.next

        temp =head

        if n==c:
            return head.next
        

        for i in range(c-n-1):
            if temp is not None:
                temp=temp.next
            
        if temp.next is not None:
            temp.next=temp.next.next

        return head
                

        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        