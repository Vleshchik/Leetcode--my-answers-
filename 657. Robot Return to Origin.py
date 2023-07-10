class Solution:
    def judgeCircle(self, moves: str) -> bool:
        koordinates = [0, 0]
        for i in moves:
            if i == 'L':
                koordinates[0] += 1
            elif i == 'R':
                koordinates[0] -= 1
            elif i == 'U':
                koordinates[1] += 1
            elif i == 'D':
                koordinates[1] -= 1
        return koordinates == [0, 0]