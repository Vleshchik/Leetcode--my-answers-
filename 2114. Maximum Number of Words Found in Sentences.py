class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for i in sentences:
            if (i.count(' ') + 1) > mx:
                mx = i.count(' ') + 1
        return mx