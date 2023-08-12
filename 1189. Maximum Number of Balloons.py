class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b':0, 'a':0, 'll': 0, 'oo':0, 'n':0}
        text = sorted(text)
        text = ''.join(text)
        for k in d.keys():
            if k in text:
                d[k] = text.count(k)
        return min(d.values())