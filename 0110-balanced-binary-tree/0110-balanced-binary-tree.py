# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root:TreeNode|None)->int:
            if root is None:
                return 0
        
        
        
            left=self.height(root.left)
            right=self.height(root.right)

            return max(left,right)+1
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        
        l=self.isBalanced(root.left)
        r=self.isBalanced(root.right)
        left=self.height(root.left)
        right=self.height(root.right)

        if abs(left-right)>1:
            return False
        
        

        return l and r
        
        
         
    
            
        
            

        
        








        