class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nums_pos = [i for i in nums if i > 0]
        nums_neg = [i for i in nums if i < 0]
        return max(len(nums_pos), len(nums_neg))