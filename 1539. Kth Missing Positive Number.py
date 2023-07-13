class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        c = 0
        i = 0
        while c != k:
            i += 1
            if i not in arr:
                c += 1

        return i