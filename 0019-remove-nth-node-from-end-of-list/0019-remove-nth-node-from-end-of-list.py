# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        c=head
        m=0
        while c:
            m=m+1
            c=c.next
        c=head

        if n==m:
            return head.next
        

        for _ in range(m-n-1):
            c=c.next

        c.next=c.next.next

        return head

        


        