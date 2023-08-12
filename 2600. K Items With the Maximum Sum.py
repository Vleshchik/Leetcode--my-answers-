class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        l = [1 for i in range(numOnes)] + [0 for i in range(numZeros)] + [-1 for i in range(numNegOnes)]
        l.sort(reverse = True)
        return sum(l[:k])