class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        c = 0
        while len(piles) > 0:
            piles.pop(0)
            c += piles.pop(0)
            piles.pop()
        return c