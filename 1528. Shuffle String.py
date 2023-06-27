class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        word = ''
        for i in range(max(indices)+1):
            word += s[indices.index(i)]
        return word