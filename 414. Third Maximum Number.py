class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) > 2:
            nums.pop(nums.index(max(nums)))
            nums.pop(nums.index(max(nums)))
        return max(nums)