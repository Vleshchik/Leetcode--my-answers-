class Solution:
    def minLength(self, s: str) -> int:
        while s.count('AB') > 0 or s.count('CD') > 0:
            s = s.replace('AB','')
            s = s.replace('CD','')
        return len(s)