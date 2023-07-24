class Solution:
    def secondHighest(self, s: str) -> int:
        l = []
        for i in s:
            if i.isdigit():
                l.append(int(i))
        if len(set(l)) == 1 or len(l) < 2:
            return -1
        else:
            mx = max(l)
            while l.count(mx) > 0:
                l.pop(l.index(max(l)))
            return max(l)