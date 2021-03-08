# https://leetcode.com/problems/design-hashmap/
# Logic: Use a hash function to put the value in a bucket. In case of collisions, extend the list

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 2048
        self.L = [[i,[]] for i in range(self.size)]
    
    def get_hash(self, number):
        # return math.floor(3000 * (number * 0.9 % 1))
        return number % self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h = self.get_hash(key)
        g = self.get(key)
        if(g == -1):
            self.L[h][1].append([key, value])
        else:
            v = self.L[h][1]
            for num in v:
                if(num[0] == key):
                    num[1] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        h = self.get_hash(key)
        v = self.L[h][1]
        for num in v:
            if(num[0] == key):
                return num[1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        h = self.get_hash(key)
        v = self.L[h][1]
        value = None
        for num in v:
            if(num[0] == key):
                value = num[1]
        if(value is not None):
            v.remove([key,value])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
