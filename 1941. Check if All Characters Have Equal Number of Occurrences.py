class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        tes = set(list(s))
        c = s.count(s[0])
        for i in tes:
            if s.count(i) != c:
                return False
        return True