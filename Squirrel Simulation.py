# https://leetcode.com/problems/squirrel-simulation/
# Logic: The only difference in path is which nut the squirrel chooses to take first. Path travelled for rest of all the nuts will remain common.
#        So the only computation is to choose which nut the squirrel should choose first. The the difference between the distance between the tree 
#        and the current nut & the distance between the current nut and the squirrel must be minimized. This gives us the minimal distance.

class Solution:
    def distance(self, x,y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        tree_nut_D = dict()
        squi_nut_D = dict()
        # tree to nuts
        mini = -float('inf')
        mini_nut = None
        total = 0
        for i in range(len(nuts)):
            tree_nut_D[tuple(nuts[i])] = self.distance(tree, nuts[i])
            squi_nut_D[tuple(nuts[i])] = self.distance(squirrel, nuts[i])
            total += (2 * tree_nut_D[tuple(nuts[i])])
            if(tree_nut_D[tuple(nuts[i])] - squi_nut_D[tuple(nuts[i])] > mini):
                mini = tree_nut_D[tuple(nuts[i])] - squi_nut_D[tuple(nuts[i])]
                mini_nut = nuts[i]
        
        return total - mini
