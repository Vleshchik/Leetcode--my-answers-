class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        c, n = 0, -inf
        for i, j in sorted(pairs, key=lambda x: x[1]):
            if n < i:
                n = j
                c += 1
        return c
