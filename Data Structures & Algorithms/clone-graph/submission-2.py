"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        new_node = Node(node.val)
        visited = {node.val: new_node}

        def dfs(root, dummy):
            for n in root.neighbors:
                if n.val in visited:
                    dummy.neighbors.append(visited[n.val])
                else:
                    d = Node(n.val)
                    visited[n.val] = d
                    dfs(n, d)
                    dummy.neighbors.append(visited[n.val])
        
        dfs(node, new_node)
        return new_node
                


        