class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = sorted([word1.count(i) for i in set(word1)])
        c2 = sorted([word2.count(i) for i in set(word2)])
        if len(word1) != len(word2) or set(word1) != set(word2) or c1 != c2:
            return False
        else:
            return True