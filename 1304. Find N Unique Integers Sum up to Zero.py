class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = []
        i = 1
        if n % 2:
            l.append(0)
            while len(l) != n:
                l.append(i)
                l.append(i * -1)
                i += 1
            else:
                return l
        else:

            while len(l) != n:
                l.append(i)
                l.append(i * -1)
                i += 1
            else:
                return l