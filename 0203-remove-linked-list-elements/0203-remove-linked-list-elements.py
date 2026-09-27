# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        c=head
        pre=None
        while c:
            if c.val==val:
                if pre is None:
                    head=c.next
                    c=head
                else:
                    pre.next=c.next
                    c=c.next
                
            else:
                pre=c
                c=c.next

        return head
        
            
           
               
            
            

        


            
            
        