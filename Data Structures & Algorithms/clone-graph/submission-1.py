"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        vis = {}

        def dfs(curr):
            if curr.val not in vis:
                clone = Node()
                clone.val = curr.val
                vis[curr.val] = clone
            
                for n in curr.neighbors:
                #for each of the neighbors, we just want to append 
                    vis[curr.val].neighbors.append(dfs(n))
                return clone

            return vis[curr.val]

        return dfs(node)



# dfs(1) -> 1, this returns the root of the cloned graph
# dfs(1) copy=2, x=dfs(2) -> 2
# dfs(2) copy=3, x=dfs(3) -> 3
# dfs(3) -> returns 3