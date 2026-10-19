class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # my idea here is that we iterate through every single entry in the 2D matrix  
        # at each entry, we check if it is land(1) and alr visited
        # if it is land and not visited, dfs from that position and increment counter

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        vis = [[False] * cols for _ in range(rows)]

        moves = [(1,0),(0,1),(-1,0), (0,-1)]
        def dfs(x, y):
            vis[x][y] = True

            for dx,dy in moves:
                nx, ny = dx + x, dy + y

                if 0 <= nx < rows and 0 <= ny < cols:

                    if not vis[nx][ny] and grid[nx][ny] == "1":
                        dfs(nx,ny)


        for i in range(rows):
            for j in range(cols):
                # if we have not visited (i,j) and its land
                # print(f"visiting ({i}, {j}), value = {grid[i][j]}")
                if not vis[i][j] and grid[i][j] == "1":
                    islands += 1
                    # we want to dfs down all of its neighbors
                    dfs(i,j)
        
        return islands



