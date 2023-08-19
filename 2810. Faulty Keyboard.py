class Solution:
    def finalString(self, s: str) -> str:
        word = ''
        for i in s:
            if i == 'i':
                word = word[::-1]
            else:
                word += i
        return word