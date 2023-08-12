class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def convert_base(n, to_base, from_base=10):
            alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res = ""
            while n > 0:
                n,m = divmod(n, to_base)
                res += alphabet[m]
            return res[::-1]
        num = convert_base(n, k)
        s = 0
        for i in num:
            s += int(i)
        return s