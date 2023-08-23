class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        l = [0,0]
        mx = 0
        for k, v in enumerate(mat):
            mx = v.count(1)
            if mx > l[1]:
                l[0] = k
                l[1] = mx
        return l