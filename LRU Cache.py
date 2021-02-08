# https://leetcode.com/problems/lru-cache/
# Logic: Use a normal hashmap/dict to store the key and value. Use another double linked list to keep the last accessed element at the start.
#.       Add and remove in D-linked list becomes 0(1)

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.dlist = list()
        self.count = 0
    
    def update(self, key):
        v = self.cache[key]
        self.dlist.remove((key, v))
        self.dlist.insert(0, (key, v))
        

    def get(self, key: int) -> int:        
        if(not key in self.cache):
            return -1
        self.update(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            old = self.cache[key]
            self.cache[key] = value
            i = self.dlist.index((key, old))
            del self.dlist[i]
            self.dlist.insert(i, (key, value))
            self.update(key)
        else:
            self.cache[key] = value
            self.dlist.insert(0, (key, value))
            self.count += 1
            if(self.count > self.capacity):
                del self.cache[self.dlist[-1][0]]
                del self.dlist[-1]
                self.count -= 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
