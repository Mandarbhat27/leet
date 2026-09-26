# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        n=0
        c=head

        while c:
            n=n+1
            c=c.next
        
        c=head

        for _ in range(n//2):
            c=c.next

        return c
        