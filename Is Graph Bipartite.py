# https://leetcode.com/problems/is-graph-bipartite/
# Logic: For each node,
#        1. If it hasn't been colored, use a color to color it. Then use the other color to color all its adjacent nodes (DFS).
#        2. If it has been colored, check if the current color is the same as the color that is going to be used to color it.
# If these condition fails return False. Also check if a node is disconnected and never colored.

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def dfs(index, value):
            if(color[index] != 0):
                return value == color[index]
            
            color[index] = value
            
            for i in range(len(graph[index])):
                if(not dfs(graph[index][i], -value)):
                    return False
            return True
        
        color = [0 for i in range(len(graph))]
        for i in range(len(graph)):
            if color[i] == 0:
                if(not dfs(i, 1)):
                    return False
        if(0 in color):
            return False
        return True
            
