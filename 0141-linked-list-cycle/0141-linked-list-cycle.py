# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c=head
        b=set()
        while c:
            if c in b:
                return True
            else:
                b.add(c)
                c=c.next
            
        return False
            
          

        

            
        