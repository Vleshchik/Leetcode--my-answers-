class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for word in words:
            if word[0] != s[0]:
                return False
            else:
                if len(s) >= len(word):
                    s = s[len(word):]
            if len(s) == 0:
                return True
        if len(s) > 0:
            return False
        else:
            return True