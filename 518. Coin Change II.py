class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for d in coins:
            for i in range(1, len(dp)):
                if i - d >= 0:
                    dp[i] += dp[i - d]
        return dp[-1] % (10 ** 10 + 7)