# https://leetcode.com/problems/rotate-image/
# Logic: Initially start by moving element by 1 position (either row number or column number increases/decreases).
#        When boundry (4 edges) is reached, change the direction and row number or column number will increase or decrease based on it.
#        Run loop (4*(end-start+1))-4 times for 1 - 90 degree rotation of outer elements.
#        Then enter the inner matrix and repeat the above steps.
#        Simpler Approach: Transpose matrix and then reverse each row 
class Solution:
    # shreyas
    def display(self,matrix):
        for i in range(0,len(matrix)):
            print(matrix[i])
            print('\n')
        print('------------------------')
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if(matrix == None or matrix[0] == None or len(matrix) == 0):
            return
        
        rotate = int(len(matrix)/2)
        n = len(matrix)
        i,j = 0,0
        start,end = 0,n-1
        while(start < end):
            rotationCount = end-start
            i,j = start,start
            while(rotationCount > 0):
                # 1 rotation
                count = (4*(end-start+1))-4
                temp,temp1 = matrix[start][start],matrix[start][start]
                rowDirection = 1
                colDirection = 0
                while(count > 0):

                    temp = temp1

                    if(i == start and j == end):
                        colDirection = 1
                        rowDirection = 0
                    elif(i == end and j == end):
                        colDirection = 0
                        rowDirection = -1
                    elif(i == end and j == start):
                        colDirection = -1
                        rowDirection = 0
                    elif(i == start and j == start):
                        pass

                    if(rowDirection > 0):
                        j += 1
                    if(rowDirection < 0):
                        j -= 1
                    if(colDirection > 0):
                        i += 1
                    if(colDirection < 0):
                        i -= 1                

                    temp1 = matrix[i][j]
                    matrix[i][j] = temp              

                    count -= 1

                    # self.display(matrix)
                rotationCount -= 1
            # print("done outer")
            start += 1
            end -= 1
