class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n = numBottles
        while numBottles // numExchange > 0:
            n += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)
        return n