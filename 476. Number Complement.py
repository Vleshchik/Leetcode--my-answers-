class Solution:
    def findComplement(self, num: int) -> int:
        s1 = bin(num)[2:]
        s2 = ''
        for i in s1:
            if i == '1':
                s2 += '0'
            else:
                s2 += '1'
        return int(s2, 2)