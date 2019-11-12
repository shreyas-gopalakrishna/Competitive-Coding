# https://leetcode.com/problems/median-of-two-sorted-arrays/solution/
# Ref: https://www.youtube.com/watch?v=LPFhl65R7ww&t=1013s
# Logic:   a b      c d
#       [2,3,9,10] [4,8,11,13] 
#       The goal is to find a combined partition on both arrays at a point such that no. of elements on left = no. of elements on right
#       Taking 4 points and comparing their values tell us if out partition should move right or left
#       Once the arrive at the correct partition, median will be (max(a,c) + min(b,d))/2 or max(a,c)
class Solution:
    # shreyas
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        if(m > n):
            nums1,nums2,m,n = nums2,nums1,n,m
        
        start = 0
        end = m
        
        while(start <= end):
            pX = int((start+end)/2)
            pY = int((m+n+1)/2 ) - pX
            
            a,b,c,d = 0,0,0,0
            
            if(pX == 0):
                a = -sys.maxsize-1
            else:
                a = nums1[pX-1]
            if(pX == m):
                b = sys.maxsize
            else:
                b = nums1[pX]
            
            if(pY == 0):
                c = -(sys.maxsize)-1
            else:
                c = nums2[pY-1]
            
            if(pY == n):
                d = sys.maxsize
            else:
                d = nums2[pY]
            
            if((a <= d) and (c <= b)):
                break
            elif(b > c):
                end = pX-1
            else:
                start = pX+1
        #print(a,b,c,d)        
        if((m+n)%2 == 0):
            return float((max(a,c) + min(b,d))/2)
        else:
            return float(max(a,c))
