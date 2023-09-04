class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mx_l = []
        tes = set(list(s))
        if len(tes) == len(s):
            return -1
        for i in tes:
            if s.count(i) > 1:
                l = [j for j in range(len(s)) if s[j] == i]
                for j in range(len(l)-1):
                    for x in range(1, len(l)):
                        mx_l.append(l[x] - l[j] - 1)
        return max(mx_l)