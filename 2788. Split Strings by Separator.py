class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        l = []
        for i in words:
            s = i.replace(separator, ' ')
            l += s.split()
        return l