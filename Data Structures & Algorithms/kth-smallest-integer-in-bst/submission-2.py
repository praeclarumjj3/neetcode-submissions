# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def _get_nodes(root):
            nodes = [root.val]        
            if root.left:
                nodes = _get_nodes(root.left) + nodes
            
            if root.right:
                nodes = nodes + _get_nodes(root.right)
            return nodes
        
        nodes = _get_nodes(root)
        
        return nodes[k-1]