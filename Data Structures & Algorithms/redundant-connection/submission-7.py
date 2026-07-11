class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(1, len(edges) + 1)}

        def has_path(node, target, visited):
            if node == target:
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    if has_path(nei, target, visited):
                        return True

            return False

        for a, b in edges:
            # If a and b are already connected,
            # this edge creates a cycle
            if has_path(a, b, set()):
                return [a, b]

            graph[a].append(b)
            graph[b].append(a)