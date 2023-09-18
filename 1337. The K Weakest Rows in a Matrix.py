class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat2 = mat.copy()
        mat2.sort(key=lambda x: sum(x))
        print(mat2)
        l = []
        for i in range(k):
            l.append(mat.index(mat2[i]))
            mat[mat.index(mat2[i])] = [2]
        return l