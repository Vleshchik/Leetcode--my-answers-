class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isOK(K):
            return sum((p-1)//K + 1 for p in piles) <= h
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if not isOK(mid):
                low = mid + 1
            else:
                high = mid
        return low