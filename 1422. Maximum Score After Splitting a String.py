class Solution:
    def maxScore(self, s: str) -> int:
        mx = 0
        for i in range(1, len(s)):
            if mx < (s[:i].count('0')+s[i:].count('1')):
                mx = s[:i].count('0')+s[i:].count('1')
        return mx