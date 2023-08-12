class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for i in word:
            if not i.isdigit():
                word = word.replace(i, ' ')
        l = map(int, word.split())
        l = set(l)
        return len(l)