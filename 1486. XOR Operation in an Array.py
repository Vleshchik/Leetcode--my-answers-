class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        num = 0
        for i in range(n):
            num ^= (start + 2 * i)
        return num
