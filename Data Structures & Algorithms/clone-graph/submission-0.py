"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # adjList = [[2],[1,3],[2]]
        if not node:
            return None
        
        old_to_new = {}

        def dfs(cur):
            if cur in old_to_new:
                return old_to_new[cur]

            copy = Node(cur.val)
            old_to_new[cur] = copy
            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node)