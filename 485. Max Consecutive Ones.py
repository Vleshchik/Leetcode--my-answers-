class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        c = 0
        for i in nums:
            if i == 1:
                c += 1
            else:
                mx = max(mx, c)
                c = 0
        mx = max(mx, c)
        return mx