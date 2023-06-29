class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        sequence1 = sequence[::-1].replace(word[::-1], '1')
        sequence2 = sequence.replace(word, '1')
        mx1 = 0
        c1 = 0
        for i in sequence1:
            if i != '1':
                if mx1 < c1:
                    mx1 = c1
                c1 = 0
            else:
                c1 += 1
        mx2 = 0
        c2 = 0
        for i in sequence2:
            if i != '1':
                if mx2 < c2:
                    mx2 = c2
                c2 = 0
            else:
                c2 += 1
        return max(max(mx1, c1), max(mx2,c2))