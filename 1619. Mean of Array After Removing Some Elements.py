class Solution:
    def trimMean(self, arr: List[int]) -> float:
        per5 = int(len(arr)/100*5)
        for i in range(per5):
            arr.pop(arr.index(max(arr)))
            arr.pop(arr.index(min(arr)))
        return sum(arr)/len(arr)