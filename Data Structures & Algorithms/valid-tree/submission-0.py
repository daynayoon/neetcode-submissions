class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if cycle detected -> False
        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        seen = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for nei in adj[node]:
                dfs(nei)

        dfs(0)
        return len(seen) == n