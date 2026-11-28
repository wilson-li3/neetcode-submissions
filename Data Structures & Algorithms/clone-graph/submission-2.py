"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        vis = {}

        def dfs(curr):
            if not curr:
                return None
            elif curr in vis:
                return vis[curr]
            else:
                copy = Node(curr.val)
                vis[curr] = copy
                for n in curr.neighbors:
                    copy.neighbors.append(dfs(n))
                return copy

        return dfs(node)

