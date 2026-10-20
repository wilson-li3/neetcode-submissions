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
        
        def dfs(currNode):
            if currNode.val in vis:
                return vis[currNode.val]

            root = Node()
            root.val = currNode.val
            vis[root.val] = root

            for n in currNode.neighbors:
                print(n.val)
                root.neighbors.append(dfs(n))

            return root

        return dfs(node)

# dfs(1) -> 1, this returns the root of the cloned graph
# dfs(1) copy=2, x=dfs(2) -> 2
# dfs(2) copy=3, x=dfs(3) -> 3
# dfs(3) -> returns 3