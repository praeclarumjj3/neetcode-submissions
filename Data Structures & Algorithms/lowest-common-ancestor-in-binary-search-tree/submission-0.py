class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lo, hi = min(p.val, q.val), max(p.val, q.val)

        while root:
            if root.val < lo:
                root = root.right
            elif root.val > hi:
                root = root.left
            else:
                return root