# https://leetcode.com/problems/surrounded-regions/
# Logic: Use DFS to go from all the border cells and visit marked. The 'O's not marked should be consumed.
class Solution:
    def capture(self, board, i, j):
        if(i >len(board)-1 or j > len(board[0])-1 or i<0 or j < 0):
            return
        if(board[i][j] == 'O'):
            board[i][j] = '1'
            self.capture(board, i+1, j)
            self.capture(board, i-1, j)
            self.capture(board, i, j+1)
            self.capture(board, i, j-1)
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == 'O'):
                    if (i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1):
                        board[i][j] = '1'
                        self.capture(board, i+1, j)
                        self.capture(board, i-1, j)
                        self.capture(board, i, j+1)
                        self.capture(board, i, j-1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == '1'):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
