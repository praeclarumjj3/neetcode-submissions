class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def _get_max_depth(node):
            if node is None:
                return 0

            left = _get_max_depth(node.left)
            right = _get_max_depth(node.right)

            self.ans = max(self.ans, left + right)

            return 1 + max(left, right)

        _get_max_depth(root)
        return self.ans