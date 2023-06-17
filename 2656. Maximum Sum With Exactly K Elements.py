class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        n = max(nums)
        for i in range(1,k):
            n += (max(nums) + i)
        return n