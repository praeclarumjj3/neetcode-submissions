class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            return (
                a.val == b.val
                and sameTree(a.left, b.left)
                and sameTree(a.right, b.right)
            )

        if subRoot is None:
            return True
        if root is None:
            return False

        return (
            sameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )