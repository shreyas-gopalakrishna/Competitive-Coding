# https://leetcode.com/problems/valid-tic-tac-toe-state/
# Logic: We need to check if X and O have taken proper turns and if anyone has won the game and no moves have been done after
#        winning.
class Solution:
    # shreyas
    def checkWin(self,board,player):
        # horizontal
        for i in range(0,3):
            if(board[i][0] == board[i][1] == board[i][2] == player):
                return True
        
        # vertical
        for i in range(0,3):
            if(board[0][i] == board[1][i] == board[2][i] == player):
                return True
        
        # left diagonal
        if(board[0][0] == board[1][1] == board[2][2] == player):
            return True
        
        #right diagonal
        if(board[0][2] == board[1][1] == board[2][0] == player):
            return True
        
        return False
    
    def validTicTacToe(self, board: List[str]) -> bool:
        counter = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 'O':
                    counter -= 1
                if board[i][j] == 'X':
                    counter += 1
        
        xWin = self.checkWin(board,'X')
        oWin = self.checkWin(board,'O')
        
        if(counter < 0 or counter > 1):
            return False
        elif(counter == 0 and xWin ):
            return False
        elif(counter == 1 and oWin):
            return False
        return True
            
