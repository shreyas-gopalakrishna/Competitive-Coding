# https://leetcode.com/problems/h-index-ii/
# Logic: Use binary search to move around. At index (n-i) will give the number of least citations the rest of list 
# has greater than this number which will be the h index.
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if(citations == None or len(citations) == 0):
            return 0
        else:
            n = len(citations)
            low = 0
            high = len(citations) - 1
            h_index = 0
            while(low <= high):
                middle = (low+high)//2
                if(middle + citations[middle] < n):
                    low = middle + 1
                else:
                    high = middle - 1
            return n - low
                
