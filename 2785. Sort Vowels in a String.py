class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        l = []
        lv = sorted([c for c in s if c in vowels])
        i = 0
        for c in s:
            if c in vowels:
                l.append(lv[i])
                i += 1
            else:
                l.append(c)
        return ''.join(l)