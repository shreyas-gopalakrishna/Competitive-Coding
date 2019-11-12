# https://leetcode.com/problems/top-k-frequent-elements/
# Logic: Count the frequency of each number and store in a Dict. Then to find the top k frequent, add them to a max heap
#        Add (-value,key) from the Dict as we want heap to be sorted according to value(frequency). -value since we need max heap.
#        Then pop k elements to get the most k frequent element.
class Solution:
    #shreyas
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        D = dict()
        for i in range(0,len(nums)):
            if nums[i] in D:
                D[nums[i]] = D[nums[i]] + 1
            else:
                D[nums[i]] = 1
        
        heap = []
        for key,value in D.items():
            heapq.heappush(heap,(-value,key))
        L = []
        for i in range(0,k):
            L.append(heapq.heappop(heap)[1])
        
        return L
