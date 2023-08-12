class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = []
        def a (s, l2):
            if len(l2) == k:
                l.append(l2.copy())
                return
            for i in range(s, n + 1):
                l2.append(i)
                a(i+1, l2)
                l2.pop()
        a(1,[])
        return l