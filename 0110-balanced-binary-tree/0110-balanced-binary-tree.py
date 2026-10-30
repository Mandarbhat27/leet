class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def height(root):
            if root is None:
                return 0

            left = height(root.left)
            right = height(root.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1