class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {idx: [] for idx in range(n)}

        for e in edges:
            a,b = e
            graph[a].append(b)
            graph[b].append(a)
        
        components = 0

        visited = set()

        def dfs(idx):
            if idx in visited:
                return
            
            visited.add(idx)
            for nei in graph[idx]:
                if nei not in visited:
                    dfs(nei)
        
        for a in range(n):
            tmp = len(visited)
            dfs(a)
            if len(visited) > tmp:
                components += 1
        
        return components
        