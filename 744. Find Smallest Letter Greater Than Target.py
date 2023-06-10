class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        mn = ord('z')
        c = 0
        for i in letters:
            if ord(i) > ord(target):
                mn = min(mn, ord(i))
                c += 1
        if c > 0:
            return chr(mn)
        else:
            return letters[0]