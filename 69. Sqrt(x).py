class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x <= 3:
            return 1
        else:
            n = x // 2
            for i in range(1,n+2):
                if (i * i) == x:
                    return i
                elif (i * i) > x:
                    return i - 1