class Solution:
    def increasingTriplet(self, n: List[int]) -> bool:
        c = False
        if len(set(n)) < 3:
            return c
        for i in range(len(n)-2):
            if n[i] == n[i+1]:
                i += 1
            else:
                for j in range(i+1, len(n)-1):
                    if n[i] < n[j]:
                        for k in range(j+1, len(n)):
                            if n[j] < n[k]:
                                c = True
                                return c
        return c