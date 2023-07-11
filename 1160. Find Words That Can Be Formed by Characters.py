class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for i in words:
            c = 0
            for j in i:
                if j in chars and i.count(j) <= chars.count(j):
                    c += 1
            if c == len(i):
                res += c
        return res