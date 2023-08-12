class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s_num = ''
        for i in s:
            s_num = s_num + str(ord(i)-96)
        for i in range(k):
            n = 0
            for j in s_num:
                n += int(j)
            s_num = str(n)
        return n