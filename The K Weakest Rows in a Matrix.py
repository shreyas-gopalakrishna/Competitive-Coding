# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/solution/
# Logic: Use binary search to find the strength(count number of 1's) in every row of the matrix. Use a heap to find the k smallest strength rows
#        Option 2 - Smart trick: Go vertically, if we find a 0 with neighbor 1, then add it to the result. Do this until we kind k and then stop. 

import math

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        def find_strength(row):
            l, r, mid = 0, n-1, None
            while(True):
                mid = int((l+r)/2)
                if(row[mid] == 1):
                    if(mid != n-1):
                        if(row[mid+1] == 0):
                            break
                    else:
                        break
                    l = mid + 1
                else:
                    if(mid <= 0):
                        break
                    r = mid -1
            if(row[mid] == 0):
                return mid
            return mid+1
        
        m,n = len(mat), len(mat[0])
        H = []
        for i in range(m):
            value = find_strength(mat[i])
            heapq.heappush(H, (value, i))
        result = []
        
        for i in range(k):
            result.append(heapq.heappop(H)[1])
        
        return result
        
        
