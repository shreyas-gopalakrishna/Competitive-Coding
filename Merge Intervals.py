# https://leetcode.com/problems/merge-intervals/
# Logic: Initialy sort the intervals based on start of interval so merging is easier and lesser comparisons needed.
#        Every time check if the i+1 interval overlaps with the i interval. If yes then merge, else move to check next element.
class Solution:
    # shreyas
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if(intervals == None or len(intervals) <= 1):
            return intervals
        
        intervals.sort(key=lambda x: x[1]) # secondary element first
        intervals.sort(key=lambda x: x[0]) # primary element next
                
        i = 0
        while(i < len(intervals)-1):
            if(intervals[i][0] <= intervals[i+1][0] and intervals[i][1] >= intervals[i+1][0]): # i+1 interval is full in between ith interval
                intervals[i] = [min(intervals[i][0],intervals[i+1][0]),max(intervals[i][1],intervals[i+1][1])]
                del intervals[i+1]
            elif(intervals[i+1][0] <= intervals[i][1] and intervals[i][0] <= intervals[i+1][0] and intervals[i][1] <= intervals[i+1][0]): # i+1 interval overlaps i interval
                intervals[i] = [min(intervals[i][0],intervals[i+1][0]),max(intervals[i][1],intervals[i+1][1])]
                del intervals[i+1]
            else:
                i+=1
            if(i == len(intervals)-1):
                break        
        return intervals
        
