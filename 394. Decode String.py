class Solution:
    def decodeString(self, s: str) -> str:
        n = 0
        string = ''
        l = []
        for c in s:
            if c.isdigit():
                n = n*10 + int(c)
            elif c == "[":
                l.append(string)
                l.append(n)
                string = ''
                n = 0
            elif c.isalpha():
                string += c
            elif c == ']':
                n2 = l.pop()
                s0 = l.pop()
                string = s0 + n2 * string
        return string