class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s2 = s * 2
        s2 = s2[1:-1]
        return s in s2