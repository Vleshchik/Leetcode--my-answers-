class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = {}
        for i in range(lowLimit, highLimit+1):
            if d.get(sum([int(j) for j in str(i)])):
                d[sum([int(j) for j in str(i)])] += 1
            else:
                d[sum([int(j) for j in str(i)])] = 1
        return max([v for v in d.values()])