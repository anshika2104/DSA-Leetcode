class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island=0
        n=len(grid)
        m=len(grid[0])
        def bfs(i,j):
            queue=deque([(i,j)])
            grid[i][j]='-1'
            dir=[(-1,0),(1,0),(0,1),(0,-1)]
            while queue:
                row,col=queue.popleft()
                for dr,dc in dir:
                    nr=row+dr
                    nc=col+dc
                    if 0<=nr<n and 0<=nc<m and grid[nr][nc]=='1':
                        queue.append((nr,nc))
                        grid[nr][nc]='-1'
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    island+=1
                    bfs(i,j)
        return island



    
        