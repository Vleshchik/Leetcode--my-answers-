class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        cities = [0] * n

        for a, b in roads:
            cities[a] += 1
            cities[b] += 1

        s = set()
        for r in roads:
            s.add(tuple(sorted(r)))

        res = 0
        for u in range(n):
            for v in range(u + 1, n):
                ans = cities[u] + cities[v]
                ans -= tuple(sorted([u, v])) in s
                res = max(res, ans)

        return res