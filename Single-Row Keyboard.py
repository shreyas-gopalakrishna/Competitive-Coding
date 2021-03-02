# https://leetcode.com/problems/single-row-keyboard/
# Logic: Store index in a hashmap

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        D = dict()
        for i in range(len(keyboard)):
            D[keyboard[i]] = i
        
        count = 0
        for i in range(len(word)):
            if(i == 0):
                count = D[word[i]]
            else:
                count += abs(D[word[i]] - D[word[i-1]])
        return count
