# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, max_value: int = -1000) -> int:
        num_good = 0
        if root is None:
            return 0
        elif root.val >= max_value:
            num_good += 1
            max_value = root.val

        num_good = num_good + self.goodNodes(root.right, max_value) + self.goodNodes(root.left, max_value) 
        
        return num_good
        