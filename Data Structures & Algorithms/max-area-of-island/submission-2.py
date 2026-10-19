class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        area = 0
        curr = 0

        moves = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(x,y):
            nonlocal curr
            grid[x][y] = 0
            curr += 1
            for dx, dy in moves:
                nx, ny = dx + x, dy + y
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] != 0:
                        dfs(nx,ny)
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j)
                    area = max(area, curr)
                    curr = 0
        
        return area
