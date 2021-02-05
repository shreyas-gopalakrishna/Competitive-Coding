# https://leetcode.com/problems/simplify-path/
# Logic: Use stack to add and remove based on path. Combine what is left at the end

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        path_split = path.split('/')
        
        for i in range(len(path_split)):
            if(path_split[i] != ''
              and path_split[i] != '.' and path_split[i] != '..'):
                stack.append(path_split[i])
            if(path_split[i] == ".." and len(stack) > 0):
                stack.pop(-1)
        return '/' + '/'.join(stack)
