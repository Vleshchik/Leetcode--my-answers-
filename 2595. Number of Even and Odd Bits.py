class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        l = [0,0]
        n = bin(n)[2:]
        n = n[::-1]
        for i in range(len(n)):
            if n[i] == '1':
                if i % 2:
                    l[1] += 1
                else:
                    l[0] += 1
        return l