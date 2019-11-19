# https://leetcode.com/problems/number-of-islands/
# Logic: Need to visit a cell containing 1 and then all its neighbours [Left Right Top Bottom]. Once a cell is visited, it is marked
#        so that we don't visit it again. Each time a cell which is unvisited and may form an island(1) is chosen to continue searhcing.
class Solution:
    # shreyas
    def island(self, grid, i, j):
        if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])):
            return
        
        if(grid[i][j] == '0' or grid[i][j] == 'X'):
            return
        
        grid[i][j] = 'X'
        self.island(grid,i+1,j)
        self.island(grid,i,j+1)
        self.island(grid,i-1,j)
        self.island(grid,i,j-1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j] == '1'):
                    self.island(grid,i,j)
                    count += 1
        
        return count
        
