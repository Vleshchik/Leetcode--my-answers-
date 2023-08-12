class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = []
        for i in range(len(prices)):
            for j in range(i + 1,len(prices)):
                if prices[i] >= prices[j]:
                    l.append(prices[i] - prices[j])
                    break
                else:
                    if j == len(prices)-1:
                        l.append(prices[i])
        l.append(prices[-1])
        return l