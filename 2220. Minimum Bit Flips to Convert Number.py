class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        c = 0
        s = bin(start)[2:]
        g = bin(goal)[2:]
        while len(s) != len(g):
            if len(s) < len(g):
                s = '0' + s
            else:
                g = '0' + g
        for i in range(len(s)):
            if s[i] != g[i]:
                c += 1
        return c