# https://leetcode.com/problems/pascals-triangle/
# Logic: Use previous list to compute next row

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if(numRows == 0):
            return []
        L = []
        if(numRows >= 1):
            L.append([1])
        if(numRows >= 2):
            L.append([1, 1])
            for i in range(3, numRows+1):
                x = []
                for i in range(len(L[-1])):
                    if(i == 0):
                        x.append(1)
                    else:
                        x.append(L[-1][i] + L[-1][i-1])
                x.append(1)
                L.append(x)
        return L
            
        
