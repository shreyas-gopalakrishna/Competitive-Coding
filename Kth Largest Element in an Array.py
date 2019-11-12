# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Logic: Use a min heap. Maintain the size of the heap to be k. If a larger number is found pop from the heap and insert that number
#        After using all numbers, the heap will have the largest k elements. Then pop gives the kth largest element. 
class Solution:
    #shreyas
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if(nums == None):
            return nums
        elif(len(nums) == 0):
            return -1        
        heap = list()
        heap.append(nums[0])
        
        heapq.heapify(heap)
        
        for i in range(1,len(nums)):
            if(len(heap) >= k):
                a = heapq.heappop(heap)
                heapq.heappush(heap,max(a,nums[i]))
            else:
                heapq.heappush(heap,nums[i])
        return heapq.heappop(heap)
