class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = 0
        for i in range(1, len(nums) + 1):
            if len(nums) % i == 0:
                n += nums[i-1] ** 2
        return n