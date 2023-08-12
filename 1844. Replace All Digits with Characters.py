class Solution:
    def replaceDigits(self, s: str) -> str:
        word = ''
        for i in range(len(s)):
            if s[i].isdigit():
                word += chr(ord(s[i-1]) + int(s[i]))
            else:
                word += s[i]
        return word