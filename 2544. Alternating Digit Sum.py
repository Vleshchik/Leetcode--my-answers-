class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n_res = 0
        while n > 0:
            if len(str(n))%2 != 0:
                n_res += (n%10)
            else:
                n_res -= (n%10)
            n = n // 10
        return n_res