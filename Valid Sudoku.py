# https://leetcode.com/problems/valid-sudoku/
# Logic: Check every column, every row and then every 3x3 block.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check(board,check_type):
            for i in range(9):
                D = dict()
                for j in range(9):
                    if(check_type == "col"):
                        if board[i][j] != "." and board[i][j] in D:
                            return False
                        else:
                            D[board[i][j]] = 1
                    else:
                        if board[j][i] != "." and board[j][i] in D:
                            return False
                        else:
                            D[board[j][i]] = 1
            return True
        
        def check_inner(board):
            for k in range(0, 9, 3):
                for l in range(0, 9, 3):
                    D = dict()
                    for i in range(k, k+3):
                        for j in range(l, l+3):
                            if board[i][j] != "." and board[i][j] in D:
                                    return False
                            else:
                                D[board[i][j]] = 1
            return True
        
        return check(board, "col") and check(board, "row") and check_inner(board)
