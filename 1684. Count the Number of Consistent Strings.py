class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = len(words)
        for i in words:
            t = list(set(i))
            for j in sorted(t):
                if j not in allowed:
                    c -= 1
                    break
        return c