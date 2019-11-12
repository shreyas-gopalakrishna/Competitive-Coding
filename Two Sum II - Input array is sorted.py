# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    # shreyas
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers
        i,j = 0,len(numbers)-1
        
        while(i < j):
            if(numbers[i]+numbers[j] == target):
                return [i+1,j+1]
            elif(numbers[i]+numbers[j] < target):
                i+=1
            else:
                j-=1        
        
        # using hash table
        # d = dict()
        # for i in range(0,len(numbers)):
        #     if(target-numbers[i] in d):
        #         return [d[target-numbers[i]], i+1]
        #     d[numbers[i]] = i+1
        
