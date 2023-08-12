class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = collections.defaultdict(int)
        ans = 0
        for a, b in dominoes:
            if a > b: a, b = b, a
            v = 10 * a + b
            ans += cnt.get(v,0)
            cnt[v] += 1
        return ans