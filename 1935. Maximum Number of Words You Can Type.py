class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        unbrokenWords = 0
        for i in text:
            c = 0
            for j in i:
                if j in brokenLetters:
                    c += 1
            if c == 0:
                unbrokenWords += 1
        return unbrokenWords
