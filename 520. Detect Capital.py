class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if (word.isupper() or word.islower() or word == word.capitalize()) else False