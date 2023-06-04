class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = []
        max_s = word1 if len(word1) > len(word2) else word2
        for i in range(min(len(word1), len(word2))):
            s.append(word1[i])
            s.append(word2[i])
            max_s = max_s[1:]
        s.append(max_s)
        return ''.join(s)