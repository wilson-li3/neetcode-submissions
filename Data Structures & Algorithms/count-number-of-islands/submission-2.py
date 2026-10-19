class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # my idea here is that we iterate through every single entry in the 2D matrix  
        # at each entry, we check if it is land(1) and alr visited
        # if it is land and not visited, dfs from that position and increment counter

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        vis = [[False] * cols for _ in range(rows)]

        def dfs(x, y):
            vis[x][y] = True
            if x > 0 and grid[x-1][y] == "1" and not vis[x-1][y]:
                dfs(x-1, y)
            if x < rows - 1 and grid[x+1][y] == "1" and not vis[x+1][y]:
                dfs(x+1, y)
            if y > 0 and grid[x][y-1] == "1" and not vis[x][y-1]:
                dfs(x, y-1)
            if y < cols - 1 and grid[x][y+1] == "1" and not vis[x][y+1]:
                dfs(x, y+1)


        for i in range(rows):
            for j in range(cols):
                # if we have not visited (i,j) and its land
                # print(f"visiting ({i}, {j}), value = {grid[i][j]}")
                if not vis[i][j] and grid[i][j] == "1":
                    islands += 1
                    # we want to dfs down all of its neighbors
                    dfs(i,j)
        
        return islands



