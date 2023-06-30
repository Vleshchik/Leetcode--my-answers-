class Solution:
    def totalMoney(self, n: int) -> int:
        c = 0
        monday = 1
        daily = 1
        for i in range(1, n+1):
            c += daily
            daily += 1
            if i % 7 == 0:
                monday += 1
                daily = monday
        return c
