class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        word = ''
        for i in words:
            word += i[0]
        return word == s