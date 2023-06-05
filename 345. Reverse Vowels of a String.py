class Solution:
    def reverseVowels(self, s: str) -> str:
        s_r = ''
        s_rev = s[::-1]
        vowels = 'aeuioAEUIO'
        for i in range(len(s_rev)):
            if s_rev[i] in vowels:
                s_r += s_rev[i]
        s = list(s)
        if len(s_r) > 0:
            for i in range(len(s)):
                if s[i] in vowels:
                    s[i] = s_r[0]
                    s_r = s_r[1:]
        return ''.join(s)

