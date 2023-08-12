class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:(len(s)//2)]
        b = s[(len(s)//2):]
        vowels = 'aeuioAEUIO'
        a_v = 0
        b_v = 0
        for i in a:
            if i in vowels:
                a_v += 1
        for i in b:
            if i in vowels:
                b_v += 1
        return a_v == b_v