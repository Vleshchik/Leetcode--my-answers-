class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        l = [max(nums)]
        nums.pop(nums.index(max(nums)))
        while sum(l) <= sum(nums):
            l.append(max(nums))
            nums.pop(nums.index(max(nums)))
        return l