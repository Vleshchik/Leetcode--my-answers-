class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        mx = start
        for i in range(len(gain)):
            start += gain[i]
            if start > mx:
                mx = start
        return mx