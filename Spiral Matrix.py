# https://leetcode.com/problems/spiral-matrix/
# Logic: Taking 4 directions and based on it increment i,j accordingly. Also taking 4 boundry variables which indicate until which index the pointer must move
#        The boundry variables are updated when a boundry is reached at each spiral. A counter is used to break once all elements are covered. 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        
        count = m*n
        i, j = 0,0
        b1, b2, b3, b4 = n-1, m-1, 0, 1
        direction = 1
        L = []
        
        while(count > 0):
            L.append(matrix[i][j])
            
            if(direction == 1 and j == b1):
                direction = 2
                b1 -= 1
            elif(direction == 2 and i == b2):
                direction = 3
                b2 -= 1
            elif(direction == 3 and j == b3):
                direction = 4
                b3 += 1
            elif(direction == 4 and i == b4):
                direction = 1
                b4 += 1
            
            if(direction == 1):
                j += 1
            elif(direction == 2):
                i += 1
            elif(direction == 3):
                j -= 1
            else:
                i -= 1
                
            count -= 1
        return L
