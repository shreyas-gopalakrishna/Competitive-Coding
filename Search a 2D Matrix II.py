# https://leetcode.com/problems/search-a-2d-matrix-ii/
# Logic: Best approach: Start from left end corner of the matrix. IF the target is more, increment the col. If target is less, decrement the row
#        This way we can reach the target faster. If not found we move out of the matrix, then return false.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False


# My approach (not the best): Have 4 pointers at the corners. If the target is not between the first 2 row pointers, move them down by a row.
# If they are not between the second 2 row pointers, move them up. Move pointers right and left similarly based on column values.
# Each time check if we have matched the target then return true, else if we find that target is less than the lowest element(p1) or greater 
# than the largest element(p4) then return false. If points cross each other, return false since it is not found.

class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m,n = len(matrix), len(matrix[0])
        
        if(m < 2 or n < 2):
            for i in range(m):
                for j in range(n):
                    if(matrix[i][j] == target):
                        return True
            return False
            
        
        p1, p2, p3, p4 = [0,0], [0,len(matrix[0])-1], [len(matrix)-1,0], [len(matrix)-1, len(matrix[0])-1]
        
        found = False
        while(p1[0] <= p2[0] or p3[0] <= p4[0] or p1[1] <= p3[1] or p2[1] <= p4[1]):
            # print("start",p1,p2,p3,p4)
            
            try:
                if(target == matrix[p1[0]][p1[1]] or target == matrix[p2[0]][p2[1]] or target == matrix[p3[0]][p3[1]] or target == matrix[p4[0]][p4[1]]):
                    return True
            except:
                pass
            
            try:
                if(target > matrix[p4[0]][p4[1]] or target < matrix[p1[0]][p1[1]]):
                    return False
            except:
                pass
            
            if(not (target > matrix[p1[0]][p1[1]] and target < matrix[p2[0]][p2[1]])):
                # print("1",p1,p2,p3,p4)
                p1[0] = p1[0] + 1
                p2[0] = p2[0] + 1
            elif(not (target > matrix[p3[0]][p3[1]] and target < matrix[p4[0]][p4[1]])):
                # print("2",p1,p2,p3,p4)
                p3[0] = p3[0] - 1
                p4[0] = p4[0] - 1
            
            elif(not (target > matrix[p1[0]][p1[1]] and target < matrix[p3[0]][p3[1]])):
                # print("3",p1,p2,p3,p4)
                p3[1] = p3[1] + 1
                p1[1] = p1[1] + 1
            elif(not (target > matrix[p2[0]][p2[1]] and target < matrix[p4[0]][p4[1]])):
                # print("4",p1,p2,p3,p4)
                p2[1] = p2[1] - 1
                p4[1] = p4[1] - 1
            
            # print("end",p1,p2,p3,p4)
        
        return False
            
            
        
        

