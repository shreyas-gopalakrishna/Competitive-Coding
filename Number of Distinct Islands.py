# https://leetcode.com/problems/number-of-distinct-islands/
# Logic: Use DFS to visit all the islands. To check if the islands are distinct, check the direction of traversal of each island. 
#        If the direction is same, then they are similar. Count the ones not same.

class Solution:    
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def getIslandGrid(grid, m, n, i, j, S):
            if( i < 0 or j < 0 or i >= m or j >= n):
                return
            if(grid[i][j] == 0 or grid[i][j] == 'X'):
                return

            grid[i][j] = 'X'

            L.append(S)

            getIslandGrid(grid, m, n, i-1, j, "U")

            getIslandGrid(grid, m, n, i+1, j, "D")

            getIslandGrid(grid, m, n, i, j+1, "R")

            getIslandGrid(grid, m, n, i, j-1, "L")

            L.append("0")
        
        m,n = len(grid), len(grid[0])
        result = set()
        for i in range(m):
            for j in range(n):
                if(grid[i][j] != 0):
                    L = []
                    getIslandGrid(grid, m, n, i, j, "0")
                    if(len(L) > 0):
                        result.add(''.join(L))
        return len(result)
                    
