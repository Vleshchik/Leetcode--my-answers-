class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        l = []
        while len(nums) > 0:
            mx = nums.pop(nums.index(max(nums)))
            mn = nums.pop(nums.index(min(nums)))
            l.append((mx + mn) / 2)
        return len(set(l))