class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 < 5:
            return 100 - (purchaseAmount // 10 * 10)
        else:
            return 100 - ((purchaseAmount // 10 + 1) * 10)