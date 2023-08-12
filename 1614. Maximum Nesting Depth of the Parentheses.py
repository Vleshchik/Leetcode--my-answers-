class Solution:
    def maxDepth(self, s: str) -> int:
        c = 0
        mx = 0
        for i in s:
            if i == '(':
                c += 1
            elif i == ')':
                c -= 1
            if c > mx:
                mx = c
        return mx