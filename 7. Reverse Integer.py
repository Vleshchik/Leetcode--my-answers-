class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)[0] + str(x)[1:][::-1]
            return int(x) if int(x) >= -1*(2**31-1) else 0
        else:
            x = str(x)[::-1]
            return int(x) if int(x) <= (2**31-1) else 0