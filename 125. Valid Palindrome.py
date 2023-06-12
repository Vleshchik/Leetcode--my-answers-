class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for i in s:
            if i.isalpha() is not True and i.isdigit() is not True:
                s = s.replace(i, '')
        return s == s[::-1]