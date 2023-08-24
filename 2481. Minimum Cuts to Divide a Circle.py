class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        else:
            return n if n % 2 else n // 2