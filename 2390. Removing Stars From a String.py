class Solution:
    def removeStars(self, s: str) -> str:
        if s.count('*') == (len(s)//2) and len(s)%2 == 0:
            return ''
        l = []
        for i in s:
            if i == '*':
                l.pop()
            else:
                l.append(i)
        return ''.join(l)
