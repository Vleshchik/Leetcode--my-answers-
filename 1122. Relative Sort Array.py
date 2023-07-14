class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l = []
        for i in arr2:
            if i in arr1:
                arr1.pop(arr1.index(i))
        for i in arr1:
            if i in arr2:
                arr2.insert(arr2.index(i), i)
            else:
                l.append(i)
        l.sort()
        arr2 += l
        return arr2