# https://leetcode.com/problems/word-search/
# Logic: Using DFS to match each letter until the complete word is matched. If an unmatch found, revert until previous match and continue
#        Is same as using backtracking algorithm

class Solution:
    def search(self, board, word, i, j, k):
        if(k >= len(word)):
            return True
                
        if(j - 1 >= 0 and board[i][j-1] == word[k]):
            letter = board[i][j-1]
            board[i][j-1] = "#"
            if(self.search(board, word, i, j-1, k+1)):
                return True
            else:
                board[i][j-1] = letter
        
        if(j + 1 < len(board[0]) and board[i][j+1] == word[k]):
            letter = board[i][j+1]
            board[i][j+1] = "#"
            if(self.search(board, word, i, j+1, k+1)):
                return True
            else:
                board[i][j+1] = letter
        
        if(i - 1 >= 0 and board[i-1][j] == word[k]):
            letter = board[i-1][j]
            board[i-1][j] = "#"
            if(self.search(board, word, i-1, j, k+1)):
                return True
            else:
                board[i-1][j] = letter
        
        if(i + 1 < len(board) and board[i+1][j] == word[k]):
            letter = board[i+1][j]
            board[i+1][j] = "#"
            if(self.search(board, word, i+1, j, k+1)):
                return True
            else:
                board[i+1][j] = letter
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == word[0]):
                    letter = board[i][j]
                    board[i][j] = "#"
                    if(self.search(board, word, i, j, 1)):
                        return True
                    board[i][j] = letter
        return False
