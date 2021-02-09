# https://leetcode.com/problems/peeking-iterator/
# Logic: Use the default iterator to go next and store the value. When Peeking iterator is used to peek, return that value. Then Peeking iterator is used to go next,
#        move the pointer but return the previously peeked value. The pointer always pointes one element ahead is the catch.

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked = False
        self.peekedValue = None
        
        if(self.iterator.hasNext()):
            self.peeked = True
            self.peekedValue = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if(self.peeked):
            return self.peekedValue 

    def next(self):
        """
        :rtype: int
        """
        temp = self.peek()
        if(self.iterator.hasNext()):
            self.peekedValue = self.iterator.next()
        else:
            self.peekedValue = None
        return temp
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeked and (self.peekedValue != None)
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
