class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        par=0
        row=len(grid)
        col=len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    par=par+4

                    if i>0:
                        if grid[i-1][j]==1:
                            par=par-1
                    if i<row-1:
                        if grid[i+1][j]==1:
                            par=par-1
                    if j>0:
                        if grid[i][j-1]==1:
                            par=par-1
                    
                    if j<col-1:
                        if grid[i][j+1]==1:
                            par=par-1
                    
        
        return par
        