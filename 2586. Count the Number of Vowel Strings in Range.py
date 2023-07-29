class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = 'aeuio'
        c = 0
        for i in range(left, right+1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                c += 1
        return c