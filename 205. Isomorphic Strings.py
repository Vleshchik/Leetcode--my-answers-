class Solution:
    def isIsomorphic(self, x: str, y: str) -> bool:
        d1 = {}
        d2 = {}
        if len(x) != len(y):
            return False
        else:
            for s1, s2 in zip(x, y):
                if (s1 in d1 and d1[s1] != s2) or (s2 in d2 and d2[s2] != s1):
                        return False
                d1[s1] = s2
                d2[s2] = s1
        return True