class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = 1000000
        for i in range(len(arr)-1):
            mn = min(mn, abs(arr[i] - arr[i + 1]))
        l = []
        for i in range(len(arr)-1):
            if abs(arr[i] - arr[i + 1]) == mn:
                l.append([arr[i], arr[i + 1]])
        return l
