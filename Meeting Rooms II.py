# https://leetcode.com/problems/meeting-rooms-ii/
# Logic: Main idea is to think in terms of priority. A room booking starting earlier will have priority over another. And if there is 
#        a overlap we will be needing another room. Hence, using a heap to always check the room which end time is the earliest. If end
#        time over laps we add to heap else pop a element(free a room and use same room). This logic works when elements are entered into
#        heap in order of start time. So sort based on it in the beginning.
class Solution:
    # shreyas
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:        
        if(intervals == None):
            return 0
        if(len(intervals) == 0 or len(intervals) == 1):
            return len(intervals)
        
        intervals.sort(key=lambda x: x[1])
        intervals.sort(key=lambda x: x[0])
        
        heap = []
        heapq.heappush(heap,(intervals[0][1],(intervals[0][0])))
        
        count = 0
        for i in range(1,len(intervals)):
            if(heap[0][0] <= intervals[i][0]):
                heapq.heappop(heap)
            heapq.heappush(heap,(intervals[i][1],intervals[i][0]))
        return len(heap)
