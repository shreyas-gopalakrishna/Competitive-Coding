# https://leetcode.com/problems/container-with-most-water/
# Logic: Take 2 pointers, start and end, and move them such that we retain 
#        the height which is more and keep updating the area
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        maxi,maxj = i,j
        maxA = 0
        while(i < j):
            A = min(height[i],height[j]) * (j-i)
            if(A > maxA):
                maxA = A
            if(height[i] < height[j]):
                i+=1
            else:
                j-=1
        return maxA
