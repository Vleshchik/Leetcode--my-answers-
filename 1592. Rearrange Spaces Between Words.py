class Solution:
    def reorderSpaces(self, text: str) -> str:
        l = text.split()
        s = text
        if ' ' in s and len(l) > 1:
            n = text.count(' ') // (len(l) - 1)
            s = (' '*n).join(l)
            if s.count(' ') < text.count(' '):
                s += ' '*(text.count(' ')-s.count(' '))
        elif ' ' in s and len(l) == 1:
            s = l[0] + ' ' * text.count(' ')
        return s