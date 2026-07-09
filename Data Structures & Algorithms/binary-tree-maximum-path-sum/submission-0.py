class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")

        def dfs(node):
            if node is None:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # path using this node as the highest/middle point
            self.ans = max(self.ans, node.val + left + right)

            # path we return to parent: can only choose one side
            return node.val + max(left, right)

        dfs(root)
        return self.ans