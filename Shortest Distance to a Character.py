# https://leetcode.com/problems/shortest-distance-to-a-character/
# Logic: Traverse the array from left to right and again from right to left to find the index of the nearest char. Choose and update the minimum

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = list()
        seen = float('inf')
        for i in range(len(s)):
            if(s[i] == c):
                answer.append(0)
                seen = i
            else:
                answer.append(abs(seen - i))        
        seen = -float('inf')
        for i in range(len(s)-1, -1, -1):
            if(answer[i] != 0):
                answer[i] = min(answer[i], abs(seen - i))
            else:
                seen = i        
        return answer
