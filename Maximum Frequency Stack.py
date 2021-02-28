# https://leetcode.com/problems/maximum-frequency-stack/
# Logic: We need to keep track of the frequency of each element, order of insert (stack order) and the current max frequent. The main conditions to handle are 
#        elements with same frequency, and elements which reach same frequency.
#        Solution is to use a map of stacks. The key will be the frequency and value will the all the elements in that frequency. A seprate dict is used to keep
#        track of the frequency of each element. During insert update count in frequency dict, update max frequency, and insert element in the map of stacks.
#        During pop, pop element from the map of stacks, update count in frequency dict and in case max frequency has changed, reduce it.

class FreqStack:

    def __init__(self):
        self.D = collections.Counter()
        self.F = collections.defaultdict(list)
        self.maxf = 0

    def push(self, x: int) -> None:
        count = self.D[x] + 1
        self.D[x] = count
        if(count > self.maxf):
            self.maxf = count
        self.F[count].append(x)

    def pop(self) -> int:
        ele = self.F[self.maxf].pop()
        self.D[ele] = self.D[ele] - 1
        if(not len(self.F[self.maxf]) > 0):
            self.maxf -= 1
        return ele
