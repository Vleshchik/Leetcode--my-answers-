class Solution:
    def isFascinating(self, n: int) -> bool:
        n = str(n) + str(2 * n) + str(3 * n)
        n = ''.join(sorted(n))
        return n == '123456789'