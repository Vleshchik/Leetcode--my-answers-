class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = max(nums)
        nums.pop(nums.index(mx))
        return (mx - 1) * (max(nums) - 1)