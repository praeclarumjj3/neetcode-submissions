class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                # Going back to the node we came from is normal
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        # Ensure every node was reachable
        return len(visited) == n