class Solution:
    def modifyString(self, s: str) -> str:
        alph = 'qwertyuiopljhgkfdsazxcvbnm'
        for i in s:
            if i in alph:
                alph = alph.replace(i, '')
        while s.count('?') > 0:
            s = s.replace('?',alph[0],1)
            alph = alph[1:]
            if len(alph) == 0:
                alph = 'qwertyuiopljhgfkdsazxcvbnm'
        return s