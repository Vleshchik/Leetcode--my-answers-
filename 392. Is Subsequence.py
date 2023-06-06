class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        w = s
        c = 0
        for i in range(len(t)):
            if len(w) > 0:
                if t[i] == w[0]:
                    w = w[1:]
                    c += 1
        if len(s) == c:
            return True
        else:
            return False