class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        l = []
        for i in range(len(arr)):
            if arr[i] == 0:
                l.append(i)

        for i in l[::-1]:
            arr.insert(i, 0)
            arr.pop(-1)
        """
        Do not return anything, modify arr in-place instead.
        """