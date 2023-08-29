class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def string_to_num(s):
            n = ''
            for i in s:
                n += str(ord(i) - 97)
            return int(n)
        return (string_to_num(firstWord) + string_to_num(secondWord)) == string_to_num(targetWord)