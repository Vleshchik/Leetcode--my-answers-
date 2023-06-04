class Solution:
    def gcdOfStrings(self, s: str, t: str) -> str:
        x = ''
        for i in range(len(t), 0, -1):
            if t[0:i] in s:
                x = t[0:i]
                if len(s.replace(x, ''))== 0 and len(t.replace(x, ''))== 0:
                    break
                else:
                    x = ''
        return x
