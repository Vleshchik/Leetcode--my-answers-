class Solution:
    def splitNum(self, num: int) -> int:
        s_n = str(num)
        s_n = sorted(s_n)
        n1 = 0
        n2 = 0
        c = 0
        for i in s_n:
            if c == 0:
                n1 *= 10
                n1 += int(i)
                c = 1
            else:
                n2 *= 10
                n2 += int(i)
                c = 0
        return n1 + n2