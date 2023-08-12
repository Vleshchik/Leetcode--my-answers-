class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = max(nums)
        c = nums.index(max(nums))
        nums.pop(nums.index(max(nums)))
        if max(nums) > 0:
            if n / max(nums) < 2:
                return -1
        return c