class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) > 2:
            nums.pop(nums.index(min(nums)))
            return min(nums)
        else:
            return -1