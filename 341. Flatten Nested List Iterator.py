# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from collections import deque

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = deque()
        self.prepareStack(nestedList)

    def next(self) -> int:
        if not self.hasNext():
            return None
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            lst = self.stack.pop().getList()
            self.prepareStack(lst)
        return bool(self.stack)

    def prepareStack(self, nestedList):
        for i in range(len(nestedList)-1, -1, -1):
            self.stack.append(nestedList[i])
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())