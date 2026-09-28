# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:

        def mir(l: TreeNode | None,r: TreeNode | None) -> bool:
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            
            if l.val!=r.val:
                return False
            
            return mir(l.left,r.right) and mir(l.right,r.left)
        return mir(root.left,root.right)
        
        