class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        c = 0
        l_money = money
        for i in sorted(prices):
            if l_money >= i:
                l_money -= i
                c += 1
            if c == 2:
                return l_money
        if c < 2:
            return money