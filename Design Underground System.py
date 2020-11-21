# https://leetcode.com/problems/design-underground-system/
# Logic: Use two hashmaps, one to store start station, end station and average another to count the trips from start station, end station

from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.check_in = dict()
        self.count = defaultdict(dict)
        self.average = defaultdict(dict)       

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [t, stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time = t - self.check_in[id][0]
        if self.check_in[id][1] in self.count and stationName in self.count[self.check_in[id][1]]:
            self.average[self.check_in[id][1]][stationName] = (self.average[self.check_in[id][1]][stationName] * self.count[self.check_in[id][1]][stationName] + time) / (self.count[self.check_in[id][1]][stationName] + 1)
            self.count[self.check_in[id][1]][stationName] += 1
        else:
            self.count[self.check_in[id][1]][stationName] = 1
            self.average[self.check_in[id][1]][stationName] = time
            
        del self.check_in[id]
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ans = self.average[startStation][endStation]
        return ans
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
