# https://leetcode.com/problems/kill-process/
# Logic: Construct a tree structure with each parent process id and their children nodes with their ids. Also store these data in a hashmap for quick access
#        Use DFS on tree to kill a node(parent) and all it's childrens

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        class Node:
            def __init__(self, ppid):
                self.ppid = ppid
                self.pids = []
            
            def add_pid(self, pid):
                self.pids.append(pid)
            
            def get_pids(self):
                return self.pids
        
        D = dict()
        for i in range(len(ppid)):
            # ppid 
            n_ppid = None
            if ppid[i] in D:
                n_ppid = D[ppid[i]]
            else:
                n_ppid = Node(ppid[i])
            
            #pid
            n_pid = None
            if pid[i] in D:
                n_pid = D[pid[i]]
            else:
                n_pid = Node(pid[i])
            
            n_ppid.add_pid(n_pid)
            
            D[ppid[i]] = n_ppid
            D[pid[i]] = n_pid
        
        result = []
        
        def find(k_id):
            result.append(k_id)
            pids = D[k_id].get_pids()
            for p in pids:
                find(p.ppid)
        find(kill)
        return result
