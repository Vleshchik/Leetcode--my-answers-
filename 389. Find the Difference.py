class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1 = sum(map(ord, [i for i in s]))
        sum2 = sum(map(ord, [i for i in t]))
        return chr(sum2 - sum1)