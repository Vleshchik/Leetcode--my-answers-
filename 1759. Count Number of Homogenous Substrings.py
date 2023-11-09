class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 1000000007
        ans, count, current_char = 0, 0, '@'
        for c in s:
            count = count + 1 if c == current_char else 1
            current_char = c
            ans += count
        return ans % MOD