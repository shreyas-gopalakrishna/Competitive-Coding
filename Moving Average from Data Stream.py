# https://leetcode.com/problems/moving-average-from-data-stream/
# Logic: Implement using a circular queue to add and remove elements based on the size. Average can me taken at any point with what is left in the queue.

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.nums = [None for i in range(size)]
        self.front, self.back = -1, -1
        self.current_total = 0
        self.current_size = 0
    
    def add(self, num):
        if(self.current_size == self.size):
            self.remove()
        if(self.current_size == 0):
            self.front += 1
        self.back = (self.back+1) % self.size
        self.nums[self.back] = num
        self.current_total += num
        self.current_size += 1
    
    def remove (self):
        temp = self.nums[self.front]
        if(self.front == self.back):
            self.front, self.back = -1,-1
        else:
            self.front = (self.front + 1) % self.size
        self.current_total -= temp
        self.current_size -= 1
        return temp

    def next(self, val: int) -> float:
        self.add(val)
        return self.current_total / self.current_size
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
