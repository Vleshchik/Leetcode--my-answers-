class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(32):
            b = (n >> i) & 1
            r = r | (b << (31 - i))
        return r