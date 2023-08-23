class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)//2):
            if s[i] == s[i * -1 - 1]:
                ans += s[i]
            else:
                ans = ans + chr(min(ord(s[i]), ord(s[i * -1 - 1])))
        if len(s) % 2:
            ans = ans + s[len(s)//2] + ans[::-1]
        else:
            ans += ans[::-1]
        return ans