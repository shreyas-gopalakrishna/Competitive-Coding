# https://leetcode.com/problems/robot-bounded-in-circle/
# Logic: The big intuition in this problem is that, given a series of steps like - "GLG" going through the steps will eventually put the robot in circle after 4 iterations.
#        The circle may be formed before the 4 iterations too. But if it does not form a circle after 4 then it won't form. Another intuition is that one single iteration is 
#        enough to decide if a circle can exist. After one iteration, if the robot comes back to origin then there exists a loop. OR if the robot points to a direction other 
#        than north, then again the robot will eventually form a loop.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        D = dict()
        
        current = (0,0)
        direction = 0
        
        moves = {0: [0,1], 1: [1,0], 2: [0,-1], 3: [-1,0]}
        
        for i in range(len(instructions)):
            if(instructions[i] == 'G'):
                x = current[0] + moves[direction][0]
                y = current[1] + moves[direction][1]
                current = (x,y)
            elif(instructions[i] == 'L'):
                direction = (direction + 3) % 4
            else:
                direction = (direction + 1) % 4
        return (current == (0,0) or direction != 0)
