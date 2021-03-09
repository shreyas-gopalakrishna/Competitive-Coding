# https://leetcode.com/problems/maximal-square/
# Logic: The approach to solving this problem is identifying that a square can be formed when the 3 adjacent squares also have 1. And this series should continue.
#        To solve this using DP we find that A max square until point (i,j) is min([i-1,j-1], [i-1,j], [i,j-1]) + 1 if (i,j) is 1.
#        At each step we also update the max size of square.
# Visualization: https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        count = 0
        
        m,n = len(matrix), len(matrix[0])
        self.visited = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == "1"):
                    self.visited[i][j] = 1 + min(self.visited[i-1][j-1], self.visited[i-1][j], self.visited[i][j-1])
                    count = max(count, self.visited[i][j])
        return count ** 2

